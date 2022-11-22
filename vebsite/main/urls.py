from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('about-us',views.about, name = 'about'),
    path('english', views.english, name = 'en'),
    path('create', views.create, name = 'create'),

    ]
