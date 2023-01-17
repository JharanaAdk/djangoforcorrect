from django.shortcuts import render

from home.models import *

# Create your views here.
def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")

def demomodels(request):
    demomodels = demomodel.objects.all()
    context = {'demomodels': demomodels}
    return render(request, "home/demo.html", context)

