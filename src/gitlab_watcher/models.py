from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
import requests

# Create your models here.

class Project(models.Model):
    project_id = models.IntegerField(verbose_name="Gitlab Project Id")
    name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=128, null=True, blank=True)
    url = models.URLField(verbose_name="Project Url:", null=True, blank=True)

    def __str__(self):
        return self.name

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
        instance.name = content["name"]
        instance.url = content["web_url"]
        instance.slug = content["path"].lower()
        instance.description = content["description"]
    except KeyError:
        raise ValueError("Project doesn't exist")

pre_save.connect(pre_save_project_reciever, Project)