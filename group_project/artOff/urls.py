from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('arena', views.arena_page),
    path('art-profile/<int:id>', views.art_profile),
    path('edit_pic', views.edit_pic),
    path('edit_info', views.edit),
    path('gallery', views.gallery_page),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('home', views.home),
    path('login_page', views.login_page),
    path('register_page', views.register_page),
    path('logout', views.logout),
    path('login', views.login),
    path('register', views.create_user),
<<<<<<< HEAD
    path('user-likes/<int:art_id>', views.likes),
    path('make_comment/<int:art:id>', views.make_comment),
=======
    path('art-profile/<int:id>', views.art_profile),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('user-likes/<int:id>', views.likes),
    path('art-comment/<int:id>', views.artComment),
    path('make_comment/<int:id>', views.make_comment),
>>>>>>> f22ed8bd990417e188f8a37897d3437ecf585ac0
    path('profile/<int:profile_id>/edit', views.edit_profile_page),
    path('delete_confirm', views.delete_confirm_page),
    path('edit_profile_page', views.edit_profile_page),
    path('edit_profile_page/update', views.update_profile),
    path('hall_of_fame_page', views.hall_of_fame_page),
    path('user_profile/<int:id>', views.user_profile_page),
    path('create_art', views.create_art)
]