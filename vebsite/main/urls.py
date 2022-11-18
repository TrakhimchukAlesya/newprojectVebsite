from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('a/',views.index2),
    ]
