from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello from Django Lab!")

def about(request):
    return HttpResponse("This is the about page of Django Lab.")

def article(request, year = 2024):
    return HttpResponse(f"This is the article page is from year {year}.")

def methods(request):
    if request.method == "GET":
        return HttpResponse("This is a GET request.")

    if request.method == "POST":
        return HttpResponse("This is a POST request.")

    return HttpResponse("Method not allowed.", status=405)

def form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        return HttpResponse(f"Hello, {name}")

    return render(request, "url_routing/form_demo.html")

