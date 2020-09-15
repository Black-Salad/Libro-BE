from rest_framework import serializers
from note.models import Note, Comment, Like


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
