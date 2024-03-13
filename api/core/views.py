from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from rest_framework import generics

from .models import User
from .serializer import *

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View para obter detalhes de um usuário específico
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View para atualizar um usuário
class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
    def update(self, request, *args, **kwargs):
        mutable_data = request.data.copy()

        if 'password' in mutable_data:
            mutable_data['password'] = make_password(mutable_data['password'])

        request.data._mutable = True
        request.data.clear()
        request.data.update(mutable_data)
        request.data._mutable = False

        return super().update(request, *args, **kwargs)

# View para excluir um usuário
class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
