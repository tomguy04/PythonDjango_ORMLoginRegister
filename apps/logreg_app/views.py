# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt

# the index function is called when root is visited

#1
def index(request):
  return render(request,"logreg_app/registrationForm.html")

def doregister(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # u1 = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'],     password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    else:
        u1 = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        u1.save()
        # request.session['id']=u1.id
        request.session['first_name']=u1.first_name
        return redirect('/dashboard')

def login(request):
    post_password = request.POST['password']
    # bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
    post_email = request.POST["email"]
    print "*****************post_email " + post_email
    print "*****************post_pass " + post_password
 
    try:
        u = User.objects.get(email = post_email)
        print "****************successful try"
       
        u.save()
        print u.id
        
        if bcrypt.checkpw(post_password.encode(), u.password.encode()):
            print "password match"
            request.session['id']=u.id
            print "*********** "
            print request.session['id']
            return redirect('/dashboard')
        return redirect('/')
    except:
        return redirect('/')
    
def dashboard(request):
    if 'id' in request.session:
        print "***************id is in session"
        u = User.objects.get(id = request.session['id'])
        user_name = u.first_name
        print "user name is " + user_name
        context = {
            'user' : user_name,
            'message' : 'you logged in.'
        }
        return render(request, "logreg_app/dashboard.html", context) 
    else:
        user_name = request.session['first_name']
        context = {
            'user' : user_name,
            'message' : 'you registerd.'
        }
        return render(request, "logreg_app/dashboard.html", context) 

def logout(request):
  request.session.clear()
  return redirect("/")

