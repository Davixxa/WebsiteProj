from django.shortcuts import render, HttpResponse, get_object_or_404 
from django.http import Http404
from .models import Project
import markdownx

# Create your views here.
def proj_list(request):
    """Render the projects page
    """
    context = {

    }
    return render(request, "project_list.html", context)

def proj_detail(request, slug=None):
    """Render a project
    """
    instance = get_object_or_404(Project, slug=slug)

    if instance.draft:
        raise Http404("Post doesn't exist")

    instance.content = markdownx.utils.markdownify(instance.content)

    context = {

        "instance": instance,

    }
    return render(request, "project_detail.html", context)
