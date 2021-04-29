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
def home(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "users" : User.objects.all(),
        "user": User.objects.get(id = request.session['user_id']),
        "arts" : Art.objects.all(),
        "test" : Art.objects.get(id=1)
    }
    return render(request, "home.html", context)
def new(request):
    return HttpResponse("LOLIT")
# ART PROFILE
def art_profile(request, id):
    one_art = Art.objects.get(id=id)
    context = {
        "art": one_art,
        "comments": Comment.objects.all()
    }
    return render(request, "art_profile.html", context)

# USER PROFILE PAGE
def user_profile_page(request, id):
    context ={
        "profile" : User.objects.get(id=id),
        "art" : Art.objects.all()
    }
    return render(request, "user_profile.html", context)

# ARENA PAGE
def arena_page(request):
    context = {
        "art" : Art.objects.all(),
        "users" : User.objects.all(),
        "me" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "arena.html", context)

# HALL OF FAME PAGE
def hall_of_fame_page(request):
    return render(request, "hall_of_fame.html")

# GALLERY PAGE 
def gallery_page(request):
    context = {
        "user" : User.objects.get(id = request.session['user_id']),
        "art" : Art.objects.all()
    }
    return render(request, "gallery.html", context)

# PROFILE EDIT PAGE
def edit_profile_page(request, profile_id):
    context = {
        "profile" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "edit_profile.html", context)

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
            request.session['username'] = users.username
            messages.success(request, "You have Successfully Logged In")
            return redirect('/home')
            print('*'*50)
            print('user made')
        return redirect('/')

# CREATE ART
def create_art(request):
    if request.method == "POST":
        errors = Art.objects.art_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print('Beginning Create of art')
            Art.objects.create(caption = request.POST['caption'], art_image = request.FILES['art_image'], artist = User.objects.get(id = request.session['user_id']))
            print('Art Has Been Made')
        return redirect('/home')

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

# LIKE METHOD
def likes(request, art_id):
    if request.method == "POST":
        likee = Art.objects.get(id=art_id)
        user = User.objects.get(id=request.session['user_id'])
        if likee.likes.all().filter(id=request.session['user_id']).exists():
            likee.likes.remove(user)
        else:
            likee.likes.add(user)
    return redirect('/home')

def make_comment(request, id):
    user = User.objects.get(id = request.session['user_id'])
    art = Art.objects.get(id = id )
    Comments.objects.create(comment = request.POST['comment'], user = user, art = art )
    return redirect('/arena')

def edit(request):
    profile = User.objects.get(id = request.session['user_id'])
    context = {
        "profile" : profile
    }
    if request.method == "POST":
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.username = request.POST['username']
        profile.quote = request.POST['quote']
        profile.email = request.POST['email']
        profile.save()
    return redirect(f'user_profile/{profile.id}')

def edit_pic(request):
    profile = User.objects.get(id = request.session['user_id'])
    context = {
        "profile" : profile
    }
    if request.method == "POST":
        profile.profile_pic = request.FILES['profile_pic']
        profile.save()
    return redirect(f'user_profile/{profile.id}')

# LOGOUT METHOD
def logout(request):
    request.session.flush()
    return redirect('/')

# DELETE METHOD
def destroy(request, art_id):
    art = Art.objects.get(id = art_id)
    if request.method == "POST":
        art.delete()
    return redirect("/home")

# UPDATE PROFILE INFORMATION
def update_profile(request):
    update_user = User.objects.get(id=request.session['user_id'])
    print(update_user)
    return redirect('/')