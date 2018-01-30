from django.db import models

# Create your models here.

class Redirect(models.Model):
    """A redirect class
    """
    slug = models.SlugField(unique=True, primary_key=True)
    url = models.URLField(verbose_name="Redirect to URL")
