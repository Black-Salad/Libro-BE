from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from django_filters import rest_framework as filter

from note.models import Note, Comment, Like
from note.serializers import NoteSerializer, NoteUserSerializer, NoteCommentSerializer, NoteLikeSerializer, NoteCommentUserjoinSerializer, NoteLikeJoinSerializer, NoteLikeCountSerializer
from django.db.models import Count, Subquery


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'note_private', 'book_id']


class NoteUserList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteUserSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'note_private', 'book_id']


class NoteListSearch(generics.ListAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter, filter.DjangoFilterBackend]
    search_fields = ['note_title', 'note_contents', 'book_title']
    filter_fields = ['user_id', 'note_private']


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


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


class NoteLikeJoin(generics.ListAPIView):
    queryset = Like.objects.values('note_id').annotate(
        cnt=Count('note_id')).order_by('-cnt')
    serializer_class = NoteLikeCountSerializer
