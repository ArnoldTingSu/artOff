from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_page', views.register_page),
    path('register', views.create_user),
    path('login_page', views.login_page),
    path('login', views.login),
    path('logout', views.logout),
    path('home', views.home_page),
    path('create_art', views.create_art),
    path('user_profile/<int:id>', views.user_profile_page),
    path('arena', views.arena_page),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('user-likes/<int:id>', views.likes),
    path('gallery', views.gallery_page),
    path('delete_confirm', views.delete_confirm_page),
]