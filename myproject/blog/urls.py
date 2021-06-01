from django.contrib import admin
from django.urls import path, re_path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path("",main,name="index"),
    path("post/<slug:slug>", page, name="page")
]
