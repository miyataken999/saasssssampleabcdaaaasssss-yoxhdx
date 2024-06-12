from django.shortcuts import render
from .models import WebSite

def index(request):
    websites = WebSite.objects.all()
    return render(request, 'index.html', {'websites': websites})