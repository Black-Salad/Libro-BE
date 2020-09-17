from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters

from note.models import Note, Comment, Like
from note.serializers import NoteSerializer, NoteCommentSerializer, NoteLikeSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.filter(note_state=True)
    serializer_class = NoteSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['user_id']
    filter_fields = ['note_private']


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteComment(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(comment_state=True)
    serializer_class = NoteCommentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['note_id']


class NoteCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = NoteCommentSerializer


class NoteLike(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = NoteLikeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ['note_id']
