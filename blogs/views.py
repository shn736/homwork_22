from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from blogs.models import Blogs


class BlogsListView(ListView):
    model = Blogs

    def get_queryset(self):
        return Blogs.objects.filter(publication_attribute=True)


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogsCreateView(CreateView):
    model = Blogs
    fields = ("header", "content", "preview")
    success_url = reverse_lazy("blogs:blogs_list")


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ("header", "content", "preview")
    success_url = reverse_lazy("blogs:blogs_list")

    def get_success_url(self):
        return reverse("blogs:blog", args=[self.kwargs.get("pk")])


class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs:blogs_list")
