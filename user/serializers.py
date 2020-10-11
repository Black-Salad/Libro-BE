from rest_framework import serializers
from .models import User, Follow, Alarm
from note.serializers import NoteSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = '__all__'


class UserFollowJoinSerializer(serializers.ModelSerializer):

    target_user_id = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['target_user_id', 'follow_id',
                  'user_id', 'follow_date']


class UserAlarmJoinSerializer(serializers.ModelSerializer):

    user_id = UserSerializer(read_only=True)
    note_id = NoteSerializer(read_only=True)

    class Meta:
        model = Alarm
        fields = ['target_user_id', 'alarm_id', 'note_id',
                  'user_id', 'alarm_date', 'alarm_type', 'alarm_state']
