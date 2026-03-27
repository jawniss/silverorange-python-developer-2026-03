import uuid

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import Posts


def index(request: HttpRequest) -> HttpResponse:
    posts = Posts.objects.select_related("author").order_by("-published_at")

    context = {"posts": posts}

    return render(request, "blog/index.html", context)


def detail(request: HttpRequest, id: uuid.UUID) -> HttpResponse:
    post = get_object_or_404(Posts.objects.select_related("author"), id=id)
    return render(request, "blog/detail.html", {"post": post})


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")
