from rest_framework import serializers
from .models import Timeline
from bookshelf.serializers import BookShelfJoinSerializer, BookStarJoinSerializer


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'


class TimelineShelfSerializer(serializers.ModelSerializer):
    shelf_id = BookShelfJoinSerializer(read_only=True)

    class Meta:
        model = Timeline
        fields = '__all__'


class TimelineStarSerializer(serializers.ModelSerializer):
    shelf_id = BookStarJoinSerializer(read_only=True)

    class Meta:
        model = Timeline
        fields = '__all__'
