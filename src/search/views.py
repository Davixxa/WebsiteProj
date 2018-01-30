from django.shortcuts import render
from django.db.models import Q
from itertools import chain

from posts.models import Post
from projs.models import Project

# Create your views here.
def search(request):
    """Render search page

        Search: projects, posts
        keys: title, content, user
    """
    query = request.GET.get("q")

    queryset_posts = Post.objects.all().order_by("-timestamp").filter(draft=0)
    queryset_projs = Project.objects.all().order_by("-timestamp").filter(draft=0)

    if query:
        queryset_posts = queryset_posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

        queryset_projs = queryset_projs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    
    queryset = sorted(chain(queryset_posts, queryset_projs),
                      key=lambda instance: instance.timestamp, reverse=True)

    context = {
        "queryset": queryset
    }

    return render(request, "search.html", context=context)
