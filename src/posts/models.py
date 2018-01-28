from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content = MarkdownxField()
    draft = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_class_name(value):
      return value.__class__.__name__
    
    class Meta:
        ordering = ["-timestamp"]    

    