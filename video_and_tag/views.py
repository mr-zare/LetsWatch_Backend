from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Video,Tag
from .serializers import VideoSerializer,TagSerializer, VideoSearchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('title', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        #print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        #print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class VideoSearchAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'tags__name']
    


class VideoListUser(generics.ListCreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Video.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
