from django.shortcuts import render
from rest_framework import generics
from .serializers.serializers import RegisterSerializer
from .models import User


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

