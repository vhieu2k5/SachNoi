from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'app/index.html')
def author(request):
    return render(request,'app/author.html')
def category(request):
    return render(
        request,'app/category.html'
    )
def discover(request):
    return render(request,'app/discover.html')