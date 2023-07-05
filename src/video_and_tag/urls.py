from .views import TagList, TagDetail, VideoSearchAPIView, VideoListUser
from django.urls import path

urlpatterns = [
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('search/', VideoSearchAPIView.as_view(), name='video_search'),
    path('videos/', VideoListUser.as_view()),
]
