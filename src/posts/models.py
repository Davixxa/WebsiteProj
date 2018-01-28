from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
