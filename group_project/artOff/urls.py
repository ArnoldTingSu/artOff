from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_page),
    path('login', views.login_page),
    path('home', views.home_page),
    path('user_profile', views.user_profile_page),
    path('arena', views.arena_page),
    path('gallery', views.gallery_page),
    path('delete_confirm', views.delete_confirm_page),
]