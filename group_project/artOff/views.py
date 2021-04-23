from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
# <----------GET---------->
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
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "art" : Art.objects.all()
    }
    return render(request, "home.html", context)

# USER PROFILE PAGE
def user_profile_page(request, id):
    context ={
        "profile" : User.objects.get(id=id)
    }
    return render(request, "user_profile.html", context)

# ARENA PAGE
def arena_page(request):
    return render(request, "arena.html")

# HALL OF FAME PAGE
def hall_of_fame_page(request):
    return render(request, "hall_of_fame.html")

# GALLERY PAGE 
def gallery_page(request):
    return render(request, "gallery.html")

# DELETE PAGE
def delete_confirm_page(request):
    return render(request, "delete_confirm.html")

# <----------POST---------->

# CREATE A USER
def create_user(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            users = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], username = request.POST['username'], email = request.POST['email'], password = pw_hash, profile_pic = request.FILES['profile_pic'])
            request.session['user_id']  = users.id
            messages.success(request, "You have Successfully Logged In")
            return redirect('/home')
            print('*'*50)
            print('user made')
        return redirect('/')

# LOGIN METHOD WITH USERNAME AND PASSWORD
def login(request):
    if request.method == "POST":
        user = User.objects.filter(username= request.POST['username'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/home')
            messages.error(request, 'Password Does Not Match')
        else:
            messages.error(request, "Username Does Not Exist")
    return redirect('/login_page')
# LOGOUT METHOD

def logout(request):
    request.session.flush()
    return redirect('/')