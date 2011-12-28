from django.views.generic import DetailView
from models import Show


class ShowDetailView(DetailView):
    queryset = Show.objects.all()
