from rest_framework import serializers
from .models import Book, Shelf, BookStar


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = '__all__'


class BookStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStar
        fields = '__all__'


class BookShelfJoinSerializer(serializers.ModelSerializer):

    book_id = BookSerializer(read_only=True)

    class Meta:
        model = Shelf
        fields = ['user_id', 'book_id',
                  'shelf_state', 'start_date', 'end_date']
