from django.urls import path
from .views import index, single_blog

urlpatterns = [
    path("", index, name= "index"),
    path("blog/<int:blog_id>/",single_blog, name= "blog"),
]
