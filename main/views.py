from django.shortcuts import render

# Create your views here.

def index(request):
    template = "main/about.html"
    return render(request,template)