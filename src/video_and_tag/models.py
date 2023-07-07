from django.db import models
from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Video(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='videos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    cover = models.FileField(default='1.png', upload_to='vid_covers')

    def str(self):
        return self.title
