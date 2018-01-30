from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
import requests

# Create your views here.
from .models import Project

@cache_page(60 * 15) # Gitlab cache comment this out while developing
def gitlab_detail(request, slug):
    if slug.isdigit():
        iid = slug
        instance = get_object_or_404(Project, project_id=iid)
    else:
        instance = get_object_or_404(Project, slug=slug.lower())
        iid = instance.project_id

    url = "https://gitlab.com/api/v4/projects/{}/repository/commits".format(iid)

    req = requests.get(url)
    content = req.json()

    context = {
        "project": instance,
        "commits": content[:50]
    }

    return render(request, "gitlab_detail.html", context=context)
