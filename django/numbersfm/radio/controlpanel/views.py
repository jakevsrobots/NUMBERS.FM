from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from radio.models import StationStatusUpdate
from forms import StationStatusUpdateForm


@user_passes_test(lambda u: u.is_active, login_url='/secrets/login/')
def dashboard(request):
    current_status = StationStatusUpdate.objects.current_status()

    if request.method == 'POST':
        form = StationStatusUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            current_status = StationStatusUpdate.objects.current_status()
            form = StationStatusUpdateForm(instance=current_status)
    else:
        form = StationStatusUpdateForm(instance=current_status)
    
    return render(request, 'radio/controlpanel/dashboard.html', {
            'current_status': current_status,
            'form': form
            })
