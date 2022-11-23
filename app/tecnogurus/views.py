from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'tecnogurus/index.html', context)

def detail(request):
    context = {}
    return render(request, "tecnogurus/detail.html", context)