from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html', {})

def counter(request):
    words = request.POST['text']
    number_of_words = len(words.split(" "))
    context = {
        "number_of_words": number_of_words
    }
    return render(request, "website/counter.html", context)

def lucy(request):
    return render(request, "website/lucy.html")

def statictest(request):
    return render(request, "website/statictest.html")

def wordcounter(request):
    return render(request, "website/wordcounter.html")