from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appDetails/', views.details, name='details'),
    path('statistics/', views.stats, name='stats'),
]
