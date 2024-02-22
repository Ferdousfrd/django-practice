from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ferdous/", views.ferdous, name="ferdous"),
    path("<str:name>", views.sayings, name="say"),
    path("htmlStuff/", views.htmlStuff, name="hs")
]

