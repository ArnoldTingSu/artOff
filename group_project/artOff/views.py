from django.shortcuts import render, HttpResponse

# Create your views here.

# LANDING PAGE
def index(request):
    return render(request, "landing.html")

# REGISTER PAGE
def register_page(request):
    return render(request, "register.html")

# LOGIN PAGE
def login_page(request):
    return render(request, "login.html")

# HOME PAGE
def home_page(request):
    return render(request, "home.html")

# USER PROFILE PAGE
def user_profile_page(request):
    return render(request, "user_profile.html")

# ARENA PAGE
def arena_page(request):
    return render(request, "arena.html")

# GALLERY PAGE 
def gallery_page(request):
    return render(request, "gallery.html")

# DELETE PAGE
def delete_confirm_page(request):
    return render(request, "delete_confirm.html")