from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Book, Shelf, BookStar
from .serializers import BookSerializer, ShelfSerializer, StarSerializer, BookShelfJoinSerializer, BookStarJoinSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['book_isbn']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ShelfList(generics.ListCreateAPIView):
    queryset = Shelf.objects.all().order_by('-start_date')
    serializer_class = ShelfSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']


class ShelfCount(generics.ListCreateAPIView):  # 책꽂이에 소지 여부 확인 시
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'book_isbn']


class ShelfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer


class StarList(generics.ListCreateAPIView):
    queryset = BookStar.objects.all().order_by('-star_add_date')
    serializer_class = StarSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id']


class StarCount(generics.ListCreateAPIView):  # 관심 여부 확인 시
    queryset = BookStar.objects.all().order_by('-star_add_date')
    serializer_class = StarSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'book_isbn']


class StarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookStar.objects.all()
    serializer_class = StarSerializer


class BookShelfJoinList(generics.ListCreateAPIView):  # 책꽂이 조회 시
    queryset = Shelf.objects.all().order_by('-start_date', 'end_date')
    serializer_class = BookShelfJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']


class BookStarJoinList(generics.ListCreateAPIView):  # 책꽂이 조회 시
    queryset = BookStar.objects.all().order_by('-star_add_date')
    serializer_class = BookStarJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id']
