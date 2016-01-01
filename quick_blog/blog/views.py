from django.views.generic import ListView

from .models import Entry


class BlogIndex(ListView):

    queryset = Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2
