from django.shortcuts import redirect, render

from .forms import NewsForm
from .models import News

# Create your views here.


def index(request):
    news = News.objects.all()
    data = {
        "title": "Home",
        "header": "Home Page",
        "news": news,
    }
    template = "main/home.html"
    return render(request, template, data)


def create_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = NewsForm()
    data = {
        "title": "Create News",
        "header": "Create News",
        "form": form,
    }
    template = "main/create_news.html"
    return render(request, template, data)
