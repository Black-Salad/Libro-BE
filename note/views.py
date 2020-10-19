from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from django_filters import rest_framework as filter

from note.models import Note, Comment, Like
from note.serializers import NoteSerializer, NoteUserSerializer, NoteCommentSerializer, NoteLikeSerializer, NoteCommentUserjoinSerializer, NoteLikeJoinSerializer, NoteLikeCountSerializer, NoteBookJoinSerializer
from django.db.models import Count, Subquery
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page_size'
    max_page_size = 100


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'note_private', 'book_id']


class NoteUserList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteUserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'note_private', 'book_id']


class NoteListSearch(generics.ListAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
    search_fields = ['note_title', 'note_contents', 'book_title']
    filter_fields = ['user_id', 'note_private']


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# NoteDetail 조회용 (book join)
class NoteDetailBookJoin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteBookJoinSerializer
    # filter_backends = [filter.DjangoFilterBackend]
    # filter_fields = ['note_id']


class NoteComment(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(comment_state=True)
    serializer_class = NoteCommentSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['note_id']


class NoteCommentUser(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(comment_state=True)
    serializer_class = NoteCommentUserjoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['note_id']


class NoteCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = NoteCommentSerializer


class NoteLike(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = NoteLikeSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['note_id', 'user_id']


class NoteLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = NoteLikeSerializer

# 좋아요 많은 독서록


class NoteLikeJoin(generics.ListAPIView):
    serializer_class = NoteSerializer

    # queryset = Like.objects.values('note_id').annotate(
    #     cnt=Count('note_id')).order_by('-cnt')[:4]

    def get_queryset(self):
        from datetime import datetime, timedelta
        today = datetime.now()
        a_month_ago = datetime.now() - timedelta(weeks=4)  # 한달전

        tmp = list(Like.objects.filter(like_date__gte=a_month_ago).filter(like_date__lte=today).values(
            'note_id').annotate(cnt=Count('note_id')).order_by('-cnt')[:4].values_list('note_id', flat=True))
        queryset = Note.objects.filter(note_id__in=tmp).filter(
            note_state=True).filter(note_private=True)
        return queryset
