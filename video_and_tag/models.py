

from django.db import models
#from django.contrib.auth.models import User
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

    def __str__(self):
        return self.title