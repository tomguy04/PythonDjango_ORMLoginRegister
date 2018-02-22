# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# the index function is called when root is visited

#1
def index(request):
  return render(request,"logreg_app/registrationForm.html")

def doregister(request):
    u1 = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
    u1.save()
    # request.session['id']=u1.id
    request.session['first_name']=u1.first_name
    return redirect('/dashboard')

def login(request):
    post_password = request.POST['password']
    post_email = request.POST["email"]
    print "*****************post_email " + post_email
    print "*****************post_pass " + post_password
 
	# user = mysql.query_db(query, data) # []
	
    # u = User.objects.get(email=post_email)
    # if  u.email == post_email:
    try:
        u = User.objects.get(email = post_email)
        print "****************successful try"
        # u = User.objects.get(email = post_email)
        u.save()
        print u.id
        print "stored pw " + u.password
        print "posted pw " + post_password
        if u.password == post_password:
            print "password match"
            request.session['id']=u.id
            print "*********** "
            print request.session['id']
            # print "***********session" + request.session['id']
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
    
    # if 'id' in request.session:
    #     print "***************id is in session
    #     context = {
    #         'user' : User.objects.get(id = request.session['id']),
    #         'message' : 'you logged in.'
    #     }
    # else:
    #     print "***************id is NOT in session
    #     context = {
    #             'user' : User.objects.get(id = request.session['id']),
    #             'message' : 'you registered.'
    #         }
        
    # return render(request, "logreg_app/dashboard.html", context) 

def logout(request):
  request.session.clear()
  return redirect("/")

