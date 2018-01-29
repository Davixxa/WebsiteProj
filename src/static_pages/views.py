from django.shortcuts import render, HttpResponse
from posts.models import Post

# Create your views here.

def index(request):
    query_set = Post.objects.all().filter(draft=0)

    for query in query_set:
         query.author = query.user.get_username()

    context = {

        "query_set": query_set

    }

    return render(request, "index.html", context)