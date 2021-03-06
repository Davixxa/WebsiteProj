from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    image = models.CharField(max_length=300, default="#")
    content = MarkdownxField()
    draft = models.BooleanField(default=True)
    math = models.BooleanField(default=True, verbose_name="Render Latex Math (using '$$' and '$' as display/inline delimiters)")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get absolute url
        Provides a common interface to reference model instances in templates,
        and enables the "view on site" button in django admin
        """
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp"]