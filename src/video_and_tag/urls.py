from .views import TagList, TagDetail, VideoSearchAPIView, VideoListUser,VideoListUser
from video_and_tag import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('videos', views.VideoViewSet)
urlpatterns = [
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('search/', VideoSearchAPIView.as_view(), name='video_search'),
    path('my-videos/', VideoListUser.as_view()),
]
urlpatterns += router.urls