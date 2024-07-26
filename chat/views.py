# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('chat:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'chat/register.html', {'form': form})

# @login_required
# def index(request):
#     return render(request, 'chat/index.html', {'users': User.objects.exclude(username=request.user.username)})

# @login_required
# def room(request, room_name):
#     return render(request, 'chat/room.html', {'room_name': room_name})


# chat/views.py

from rest_framework import generics, permissions
from .serializers import UserSerializer
from authentications.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
