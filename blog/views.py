from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.models import Authors
from blog.models import Posts


def index(request: HttpRequest) -> HttpResponse:
    # posts = Posts.objects.all().order_by('-published_at')
    posts = Posts.objects.select_related("author").order_by("-published_at")

    context = {
        "posts": posts
    }

    return render(request, "blog/index.html", context)


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")
