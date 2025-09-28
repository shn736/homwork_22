from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView

app_name = BlogsConfig.name

urlpatterns = [
    path('blogs/create', BlogCreateView.as_view(), name="blogs_create"),

]
