from django.shortcuts import render
from rest_framework import generics, viewsets, views
from django_filters import rest_framework as filter

from .models import User, Follow, Alarm
from .serializers import UserSerializer, FollowSerializer, UserFollowJoinSerializer, AlarmSerializer, UserAlarmJoinSerializer

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.mail import EmailMessage
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page_size'
    max_page_size = 100


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_email', 'user_state', 'user_name']


class RecommentUserList(generics.ListAPIView):  # 팔로우 추천 (로그인유저가 팔로우하고 있지 않은 대상)
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        target_users = list(Follow.objects.filter(user_id=user).values_list(
            'target_user_id', flat=True))
        queryset = User.objects.exclude(user_id__in=target_users).exclude(user_id=user).filter(
            user_state=True).order_by('?')[:8]
        return queryset


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
    pagination_class = StandardResultsSetPagination
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'target_user_id']


class FollowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class UserFollowJoinList(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = UserFollowJoinSerializer
    pagination_class = StandardResultsSetPagination
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


class PasswordFind(APIView):

    def post(self, request, format=None):
        user_email = self.request.query_params.get('user_email', None)
        user_pw = self.request.query_params.get('user_pw', None)
        if user_email is not None:
            email = EmailMessage('Libro🌿 회원님의 임시 비밀번호를 발급해드립니다!😊',
                                 '회원님의 임시 비밀번호는 [ '+user_pw+' ] 입니다. 로그인 후 반드시 비밀번호를 재 설정해주세요!', to=[user_email])
            email.send()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
