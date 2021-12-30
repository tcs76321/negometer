from django.http import HttpResponse, Http404
from django.shortcuts import render

from mainfunc.models import NewsOutlet


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def detail(request, tag):
    try:
        outlet = NewsOutlet.objects.get(tag=tag)
    except NewsOutlet.DoesNotExist:
        raise Http404("News Outlet does not exist")
    return render(request, '../templates/detail.html', {'outlet': outlet})


def info(request):
    context = {
    }
    return render(request, 'info.html', context)


def support(request):
    context = {
    }
    return render(request, 'support.html', context)


def contact(request):
    context = {
    }
    return render(request, 'contact.html', context)


def robots(request):
    file1 = open("robots.txt", 'r')
    robots_text = file1.read()
    return HttpResponse(content=robots_text, content_type='text/plain; charset=utf-8')
