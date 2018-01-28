from django.shortcuts import render, HttpResponse, get_object_or_404, 
from django.http import Http404
from .models import Post
import markdownx

# Create your views here.


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    
    if instance.draft:
        raise Http404("Post doesn't exist")

    instance.content = markdownx.utils.markdownify(instance.content)

    context = {
    
        "instance": instance, 
    
    }

    return render(request,"post_detail.html", context)

