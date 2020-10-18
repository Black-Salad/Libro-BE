from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Timeline
from user.models import Follow
from .serializers import TimelineSerializer, TimelineJoinSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class TimelineList(generics.ListCreateAPIView):  # 타임라인 추가할 때
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class UserTimelineGetList(generics.ListCreateAPIView):  # 타임라인 불러올 때
    serializer_class = TimelineJoinSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.query_params.get('user', None)
        target_users = list(Follow.objects.filter(user_id=user).values_list(
            'target_user_id', flat=True))
        queryset = Timeline.objects.filter(user_id__in=target_users).filter(
            tl_state=True).order_by('-tl_add_date')
        return queryset


# class TimelineJoinList(generics.ListCreateAPIView):  # 타임라인 불러올 때
#     queryset = Timeline.objects.filter(tl_state=True)
#     serializer_class = TimelineJoinSerializer
#     # filter_backends = [filter.DjangoFilterBackend]
#     # filter_fields = ['user_id']
