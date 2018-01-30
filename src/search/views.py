from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.cache import cache_page
from itertools import chain

from posts.models import Post
from projs.models import Project
from gitlab_watcher.models import GitlabProject

# Create your views here.
@cache_page(60 * 15) # 15min search cache comment this line while developing
def search(request):
    """Render search page

        Search: projects, posts
        keys: title, content, user
    """
    query = request.GET.get("q")

    queryset_posts = Post.objects.all().order_by("-timestamp").filter(draft=0)
    queryset_projs = Project.objects.all().order_by("-timestamp").filter(draft=0)
    queryset_gitlab = GitlabProject.objects.all().order_by("-timestamp")

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

        queryset_gitlab = queryset_gitlab.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    queryset = sorted(chain(queryset_posts, queryset_projs, queryset_gitlab),
                      key=lambda instance: instance.timestamp, reverse=True)

    context = {
        "queryset": queryset[:10] # limit search results default 10
    }

    return render(request, "search.html", context=context)
