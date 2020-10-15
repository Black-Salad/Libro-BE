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


class NoteCommentUserjoinSerializer(serializers.ModelSerializer):
    from user.serializers import UserSerializer
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class NoteLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class NoteLikeJoinSerializer(serializers.ModelSerializer):
    # note_id = NoteSerializer(read_only=True)
    note_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class NoteUserSerializer(serializers.ModelSerializer):
    from user.serializers import UserSerializer
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'


class CommentNoteJoinSerializer(serializers.ModelSerializer):

    note_id = NoteUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class NoteBookJoinSerializer(serializers.ModelSerializer):
    from bookshelf.serializers import BookSerializer
    book_id = BookSerializer(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
