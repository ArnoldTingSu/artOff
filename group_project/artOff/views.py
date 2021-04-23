from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("THIS IS THE PAGE!")

def landing(request):
    return render(request, "landing.html")