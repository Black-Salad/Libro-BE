from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Book, Shelf, BookStar
from .serializers import BookSerializer, ShelfSerializer, BookStarSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ShelfList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
