from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from django_filters import rest_framework as filter

from .models import Book, Shelf, BookStar
from .serializers import BookSerializer, ShelfSerializer, BookStarSerializer


# Create your views here.
