from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def demomodel(request):
    demomodels = demomodel.object.all()
    context ={'demomodels':demomodels}
    return render(request, 'home/about.html', context)