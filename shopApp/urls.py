from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appDetails/', views.details, name='details'),
    path('statistics/', views.stats, name='stats'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register_request, name="register"),
    path('purchase/', views.purchase, name="purchase"),
    path('purchase/complete/', views.complete, name="complete"),
]
