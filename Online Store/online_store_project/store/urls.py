# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='cart'),
    # Define other URL patterns
]
