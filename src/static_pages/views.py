from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from posts.models import Post
from .models import Redirect

# Create your views here.

def index(request):
    """Render the frontpage
    """
    # query_sets are lazy, so we can limit the number of
    # posts by using list-slicing, here the first 10 posts
    query_set = Post.objects.all().filter(draft=0)[:10]

    for query in query_set:
        query.author = query.user.get_username()

    context = {

        "query_set": query_set

    }

    return render(request, "index.html", context)

def about(request):
    """Render the about page
    """
    context = {

    }
    return render(request, "about.html", context)

def redirect_view(request, slug=None):
    """Redirect view which sends a 301 to a site
    """
    instance = get_object_or_404(Redirect, slug=slug)
    return redirect(instance.url)
