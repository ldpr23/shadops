from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shadopsapp/base.html')


def about(request):
    return render(request, 'shadopsapp/about.html')