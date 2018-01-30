from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField

class Project(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    image = models.CharField(max_length=300, default="#")
    content = MarkdownxField()
    custom_html = models.TextField(verbose_name="CUSTOM HTML")
    draft = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        """Get absolute url
        Provides a common interface to reference model instances in templates,
        and enables the "view on site" button in django admin
        """
        return reverse("projs:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp"]
