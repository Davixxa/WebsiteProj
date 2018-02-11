from django.shortcuts import render, HttpResponse, get_object_or_404 
from django.http import Http404
from .models import Post
import markdownx
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

def post_list(request):
    """Renders the 'blog' page
    """


    query_set = Post.objects.all().filter(draft=0)
    paginator = Paginator(query_set, 10)

    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        
        "posts": posts,
        "pages" : paginator.num_pages
        
    }
    return render(request,"post_list.html", context)