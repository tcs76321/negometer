from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:tag>/', views.detail, name='detail'),
]
