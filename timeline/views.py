from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filter
from .models import Timeline
from .serializers import TimelineSerializer, TimelineShelfSerializer, TimelineStarSerializer


class TimelineList(generics.ListCreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class TimelineShelfJoinList(generics.ListCreateAPIView):
    queryset = Timeline.objects.filter(tl_state=True)
    serializer_class = TimelineShelfSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'tl_kind']


class TimelineStarJoinList (generics.ListCreateAPIView):
    queryset = Timeline.objects.filter(tl_state=True)
    serializer_class = TimelineStarSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filter_fields = ['user_id', 'tl_kind']


class TimelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
