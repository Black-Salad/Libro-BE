from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter

# from .models import User, Shelf
# from .serializers import UserSerializer, UserShelfSerializer
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserShelf(generics.ListCreateAPIView):
#     queryset = Shelf.objects.all()
#     serializer_class = UserShelfSerializer
#     filter_backends = [filter.DjangoFilterBackend]
#     filter_fields = ['shelf_state']
