# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        elif not postData['first_name'].isalpha(): 
            errors["first_name"] = "First name must be characters only"        
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name be at least 2 characters."
        elif not postData['last_name'].isalpha(): 
            errors["last_name"] = "First name must be characters only"  
        if len(postData['email']) < 1:
            errors["email"] = "email should be at least 1 character."
        elif not EMAIL_REGEX.match( postData['email']):
            errors["email"] = "Email must be a valid format"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters."
        elif postData['password'] != postData['confpassword']:
            errors["password"] = "password and confirmation password don't match"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()


