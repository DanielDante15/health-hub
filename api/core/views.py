from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from rest_framework import generics

from .models import User
from .serializer import *


from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))

