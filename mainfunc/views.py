from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

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
