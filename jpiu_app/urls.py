from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("our-projects/", views.our_projects, name="our-projects"),
    path("news/", views.news, name="news"),
    path("news-details/<int:pk>/", views.news_details, name="news_details"),
]
