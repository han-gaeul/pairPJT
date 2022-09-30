from django.shortcuts import render



def index(request):
    return render(request, 'pairApp/index.html')


def detail(request):
    return render(request, 'pairApp/detail.html')


def new(request):
    return render(request, 'pairApp/new.html')