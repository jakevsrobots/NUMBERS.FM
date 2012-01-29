from django.http import HttpResponse
from django.views.generic import DetailView
from models import Show


def test(request):
    import commands
    output = commands.getoutput('start_ices.sh')

    return HttpResponse(output)

class ShowDetailView(DetailView):
    queryset = Show.objects.all()
