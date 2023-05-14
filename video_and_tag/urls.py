from rest_framework.routers import DefaultRouter
from .views import TagList, TagDetail
from video_and_tag import views
from django.urls import path
router = DefaultRouter()
router.register('videos', views.VideoViewSet)

urlpatterns = [
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
]

urlpatterns += router.urls