from django.urls import path
from .views import RegistrationView, LoginView, UserList

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-list/', UserList.as_view(), name='user-list'),
]
