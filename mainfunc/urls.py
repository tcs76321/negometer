from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:tag>/', views.detail, name='detail'),
    path('info/', views.info, name='info'),
    path('support/', views.support, name='support'),
    path('contact/', views.contact, name='contact'),
    path('robots.txt', views.robots, name='robots'),
]
