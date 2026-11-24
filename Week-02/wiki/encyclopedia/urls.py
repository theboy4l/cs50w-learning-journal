from os import name

from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new/", views.new_page, name="new_page"),
    path("save/", views.save_page, name="save_page"),
    path("<str:title>/", views.title, name="title"),
]
