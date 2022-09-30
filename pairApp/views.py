from django.shortcuts import redirect, render
from .models import Review



def index(request):
    reviews = Review.objects.all()

    context = {
        'reviews' : reviews
    }
    return render(request, 'pairApp/index.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review' : review
    }
    return render(request, 'pairApp/detail.html', context)


def new(request):

    return render(request, 'pairApp/new.html')

def edit(request, pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review' : review
    }
    return render(request, 'pairApp/edit.html', context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Review.objects.create(title=title, content=content)

    return redirect('pairApp:index')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get('title')
    content = request.GET.get('content')

    review.title = title
    review.content = content
    review.save()

    return redirect('pairApp:detail', review.pk)

def delete(request, pk):
    Review.objects.get(pk=pk).delete() 
    return redirect('pairApp:index')