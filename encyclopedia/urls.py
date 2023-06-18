from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("random/", views.random_article, name="random")
]
