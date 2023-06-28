from rest_framework import generics
from .models import Video, Tag
from .serializers import VideoSerializer, TagSerializer, VideoSearchSerializer
from rest_framework import viewsets
from rest_framework import filters


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('title',)
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        return obj

    def destroy(self, request, *args, **kwargs):
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
