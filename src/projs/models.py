from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    image = models.CharField(max_length=300, default="#")
    content = MarkdownxField()
    custom_html = models.TextField(verbose_name="CUSTOM HTML")
    draft = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def get_class_name(self):
      return self.__class__.__name__
    
    def __str__(self):
      return self.title

    class Meta:
        ordering = ["-timestamp"]    
