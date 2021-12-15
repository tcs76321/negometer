from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def detail(request, tag):
    return HttpResponse("You're looking at %s." % tag)
