from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login_page', views.login_page),
    path('register_page', views.register_page),
    path('logout', views.logout),
    path('login', views.login),
    path('arena', views.arena_page),
    path('register', views.create_user),
    path('art-profile/<int:id>', views.art_profile),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('user-likes/<int:id>', views.likes),
    path('make_comment/<int:art.id>', views.make_comment),
    path('profile/<int:profile_id>/edit', views.edit_profile_page),
    path('gallery', views.gallery_page),
    path('edit_info', views.edit),
    path('edit_pic', views.edit_pic),
    path('delete_confirm', views.delete_confirm_page),
    path('edit_profile_page', views.edit_profile_page),
    path('edit_profile_page/update', views.update_profile),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('user_profile/<int:id>', views.user_profile_page),
    path('create_art', views.create_art)
]