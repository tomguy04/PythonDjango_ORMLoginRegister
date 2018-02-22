# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

# class UserManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 1:
#             errors["first_name"] = "Please enter your first name"
#         if len(postData['email']) < 2:
#             errors["email"] = "email should be at least 2 characters."
#         return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    # objects = UserManager()


