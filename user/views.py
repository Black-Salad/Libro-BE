from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter

from .models import User, Follow, Alarm
from .serializers import UserSerializer, FollowSerializer, UserFollowJoinSerializer, AlarmSerializer, UserAlarmJoinSerializer

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_email', 'user_state', 'user_name']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    parser_class = (FileUploadParser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = UserSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'target_user_id']


class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class UserFollowJoinList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = UserFollowJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'target_user_id']


class AlarmList(generics.ListCreateAPIView):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer


class AlarmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer


class UserAlarmJoinList(generics.ListCreateAPIView):
    queryset = Alarm.objects.all()
    serializer_class = UserAlarmJoinSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['target_user_id', 'alarm_state']
