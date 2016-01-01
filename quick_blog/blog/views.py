from django.views.generic import ListView, DetailView

from .models import Entry


class BlogIndex(ListView):

    queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(DetailView):

    model = Entry
    template_name = "post.html"
