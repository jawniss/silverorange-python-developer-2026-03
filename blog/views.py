from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Authors
from blog.models import Posts

def index(request: HttpRequest) -> HttpResponse:
    posts = Posts.objects.select_related("author").order_by("-published_at")

    context = {
        "posts": posts
    }

    return render(request, "blog/index.html", context)

def detail(request, id):
    print(id)
    post = get_object_or_404(Posts.objects.select_related('author'), id=id)
    print("post: ", post)
    return render(request, 'blog/detail.html', {'post': post})

def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")

