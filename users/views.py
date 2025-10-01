import requests
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.models import User
from .serializers import UserSerializer


class UserCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_random_user(request):
    url = "https://randomuser.me/api/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        parsed_user = {
            "first_name": user['name']['first'],
            "last_name": user['name']['last'],
            "email": user['email'],
            "username": user['login']['username'],
            "gender": user['gender'],
            "city": user['location']['city'],
            "state": user['location']['state'],
            "country": user['location']['country']
        }
        return Response(parsed_user)
    return Response({"error": "Não foi possível obter usuário"}, status=status.HTTP_400_BAD_REQUEST)


class RnadomUserSaveView(APIView):
    def post(self, request):
        url = "https://randomuser.me/api/"
        response = requests.get(url)

        if response.status_code != 200:
            return Response({"error": "Não foi possível obter usuário"}, status=status.HTTP_400_BAD_REQUEST)

        data = response.json()
        user = data['results'][0]

        parsed_user = {
            "first_name": user['name']['first'],
            "last_name": user['name']['last'],
            "email": user['email'],
            "username": user['login']['username'],
            "gender": user['gender'],
            "city": user['location']['city'],
            "state": user['location']['state'],
            "country": user['location']['country']
        }

        serializer = UserSerializer(data=parsed_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
