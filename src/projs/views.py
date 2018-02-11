from django.shortcuts import render, HttpResponse, get_object_or_404 
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
import markdownx

# Create your views here.
def proj_list(request):
    """Render the projects page
    """

    
    query_set = Project.objects.all().filter(draft=0)
    paginator = Paginator(query_set, 10)

    page = request.GET.get("page")

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
        





    

    context = {

        "projects": projects,
        "pages" : paginator.num_pages

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
