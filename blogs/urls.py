from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import (
    BlogsCreateView,
    BlogsListView,
    BlogsDetailView,
    BlogsUpdateView,
    BlogsDeleteView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogsListView.as_view(), name="blogs_list"),
    path("blogs/<int:pk>/", BlogsDetailView.as_view(), name="blog"),
    path("blogs/create/", BlogsCreateView.as_view(), name="blogs_create"),
    path("blogs/<int:pk>/update/", BlogsUpdateView.as_view(), name="blogs_update"),
    path("blogs/<int:pk>/delete/", BlogsDeleteView.as_view(), name="blogs_delete"),
]
