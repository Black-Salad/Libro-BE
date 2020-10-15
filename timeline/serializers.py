from rest_framework import serializers
from .models import Timeline
from bookshelf.serializers import BookShelfJoinSerializer, BookStarJoinSerializer
from user.serializers import UserSerializer, UserFollowJoinSerializer
from note.serializers import NoteBookJoinSerializer, NoteLikeJoinSerializer, CommentNoteJoinSerializer


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'


class TimelineJoinSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    shelf_id = BookShelfJoinSerializer(read_only=True)
    star_id = BookStarJoinSerializer(read_only=True)
    note_id = NoteBookJoinSerializer(read_only=True)
    follow_id = UserFollowJoinSerializer(read_only=True)
    comment_id = CommentNoteJoinSerializer(read_only=True)
    like_id = NoteLikeJoinSerializer(read_only=True)

    class Meta:
        model = Timeline
        fields = '__all__'
