from django.shortcuts import render


def dashboard(request):
    return render(request, 'radio/controlpanel/dashboard.html')
                  
