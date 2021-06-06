from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from qwertyindex.models import qwertyindex


def index(request):
    template_name = 'base.html'
    return render(request, template_name)
