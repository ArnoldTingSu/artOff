from django.db import models
import re


# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First Name Must Be At Least 3 Characters Long"
        if len(postData['last_name']) < 3 :
            errors['last_name'] = "Last Name Must Be At Least 3 Characters Long"
        if len(postData['username']) < 2 :
            errors['username'] = "Username Must Be At Least 2 Characters Long"
        EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "This Email Does Not Pass The Validation Test"
        if len(postData['password']) < 8 :
            errors['password'] = "Password Must Be At Least 8 Characters Long"
        if not postData['password'] == postData['confirm_password']:
            errors['confirm_pw'] = 'Password Does Not Match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 70)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to= "images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class ArtManager(models.Manager):
    def art_validator(self, postData):
        errors = {}
        if len(postData['caption']) < 3 :
            errors['caption'] = "Please Make This About 3 Or More Characters"
        return errors

class Art(models.Model):
    caption = models.CharField(max_length = 100)
    art_image = models.ImageField(upload_to= "images/")
    user_art = models.ForeignKey(User, related_name= 'users_art', on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_post')
    objects = ArtManager()

class Comments(models.Model):
    comment = models.TextField()
    user_comment = models.ForeignKey(User, related_name = "users_comment", on_delete = models.CASCADE)
    art_comment = models.ForeignKey(Art, related_name = "art_comments", on_delete = models.CASCADE )