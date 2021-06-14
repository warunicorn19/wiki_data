from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki_data/<str:entry>", views.entry, name="entry"),
    path("newEntry", views.newEntry, name= "newEntry"),
    path("wiki_data/<str:entry>/edit", views.edit, name= "edit"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search")
    
]
