from uuid import UUID

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


def detail(request: HttpRequest, pk: UUID) -> HttpResponse:
    return render(request, "blog/detail.html")


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")
