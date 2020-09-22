from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Book, Shelf, BookStar
from .serializers import BookSerializer, ShelfSerializer, BookStarSerializer, BookShelfJoinSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ShelfList(generics.ListCreateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']


class BookShelfJoinList(generics.ListCreateAPIView):
    queryset = Shelf.objects.all()
    serializer_class = BookShelfJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']
