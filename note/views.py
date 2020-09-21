from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from django_filters import rest_framework as filter

from note.models import Note, Comment, Like
from note.serializers import NoteSerializer, NoteCommentSerializer, NoteLikeSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'note_private']


class NoteListSearch(generics.ListAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['note_title', 'note_contents', 'book_name']


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteComment(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(comment_state=True)
    serializer_class = NoteCommentSerializer
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
