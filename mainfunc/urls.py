from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abc', views.index, name='index'),
    path('cbs', views.index, name='index'),
    path('cnn', views.index, name='index'),
    path('fox', views.index, name='index'),
    path('nbc', views.index, name='index'),
    path('about', views.index, name='index'),
    path('donate', views.index, name='index'),
    path('contact', views.index, name='index'),
]