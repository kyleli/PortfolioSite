from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Kyle',
        'age': 23,
        'nationality': 'USA'
    }
    return render(request, "index.html", context)

def counter(request):
    words = request.POST['text']
    number_of_words = len(words.split(" "))
    context = {
        "number_of_words": number_of_words
    }
    return render(request, "counter.html", context)

def lucy(request):
    return render(request, "lucy.html")

def statictest(request):
    return render(request, "statictest.html")

def wordcounter(request):
    return render(request, "wordcounter.html")