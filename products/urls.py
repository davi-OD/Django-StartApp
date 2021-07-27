# this is where we map the urls to the views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_products)
]
