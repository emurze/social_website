from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def dashboard(request: WSGIRequest) -> HttpResponse:
    context = {
        'section': 'dashboard',
        'title': 'Dashboard',
    }
    return render(request, 'account/dashboard.html', context)
