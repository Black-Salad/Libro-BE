from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Book, Shelf, BookStar
from .serializers import BookSerializer, ShelfSerializer, StarSerializer, BookShelfJoinSerializer, BookStarJoinSerializer
from django.db.models import F
# ...
# MyModel.objects.filter(id=...).update(hit_count=F('hit_count')+1)
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page_size'
    max_page_size = 100


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
    queryset = Shelf.objects.all().order_by('-start_date', '-end_date')
    serializer_class = BookShelfJoinSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']


class BookStarJoinList(generics.ListCreateAPIView):  # 책꽂이 조회 시
    queryset = BookStar.objects.all().order_by('-star_add_date')
    serializer_class = BookStarJoinSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id']


class BookShelfDateFilterList(generics.ListAPIView):  # 읽은 책 기간별 조회
    queryset = Shelf.objects.all().order_by('-end_date')
    serializer_class = BookShelfJoinSerializer
    # pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filterset_fields = {
        'start_date': ['gte'],
        'end_date': ['lte'],
        'user_id': ['exact'],
        'shelf_state': ['exact'],
    }


# 페이징 없이 모두 조회 (독서록 쓰기에 책 불러오기)
class BookShelfJoinList2 (generics.ListCreateAPIView):
    queryset = Shelf.objects.all().order_by('-start_date', '-end_date')
    serializer_class = BookShelfJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'shelf_state']

# 관심 많은 책


class StarOrderedBooks (generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        from datetime import datetime, timedelta
        today = datetime.now()
        a_month_ago = datetime.now() - timedelta(weeks=4)  # 한달전

        tmp = list(BookStar.objects.filter(star_add_date__gte=a_month_ago).filter(star_add_date__lte=today).values(
            'book_id').annotate(cnt=Count('book_id')).order_by('-cnt')[:6].values_list('book_id', flat=True))
        queryset = Book.objects.filter(book_id__in=tmp)
        return queryset
