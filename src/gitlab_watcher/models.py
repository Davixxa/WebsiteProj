from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
import requests

# Create your models here.

class GitlabProject(models.Model):
    project_id = models.IntegerField(verbose_name="Gitlab Project Id")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=128, null=True, blank=True)
    url = models.URLField(verbose_name="Project Url:", null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Get absolute url
        Provides a common interface to reference model instances in templates,
        and enables the "view on site" button in django admin
        """
        return reverse("gitlab:detail", kwargs={"slug": self.slug})

def pre_save_project_reciever(sender, instance, *args, **kwargs):
    """Do project validation
    """
    r = requests.get("https://gitlab.com/api/v4/projects/"+str(instance.project_id))
    try:
        content = r.json()
        instance.title = content["name"]
        instance.url = content["web_url"]
        instance.slug = content["path"].lower()
        instance.description = content["description"]
        instance.timestamp = content["created_at"]
    except KeyError:
        raise ValueError("Project doesn't exist")

pre_save.connect(pre_save_project_reciever, GitlabProject)