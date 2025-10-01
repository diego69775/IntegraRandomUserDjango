from django.urls import path
from . import views


urlpatterns = [
    path('randomuser/', views.get_random_user, name='get-random-user'),
    path('randomuser/save/', views.RnadomUserSaveView.as_view(), name='random-user-save'),
    path('users/', views.UserCreateListView.as_view(), name='user-create-list'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-retrive-update-destroy'),
]
