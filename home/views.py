# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from forms import *
from models import *
from django.contrib import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Create your views here.
def index(request):
    return render(request,'learn/learn.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})
def forgotpassword(request):
    if request.method == 'POST':
        form=ForgotpasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user_num=User.objects.filter(username=username,email=email).count()
            
            if user_num > 0 :
                user=User.objects.get(username=username,email=email)
                s=""
                s="qwer123"
                user.set_password('qwer123')
                user.save()
                return render(request,'forgotpassword/changepasswordsuccess.html',{'password':s})
            else :
                return render(request,'forgotpassword/changepaswordunsuccess.html')
    else:
        form=ForgotpasswordForm
        return render(request,'forgotpassword/forgotpassword.html',{'form': form})


def profile(request):
    #print request.user.id
    return render(request,'userdetails/profile.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user=request.user
        #user_form = UserForm(request.POST, instance=request.user)
        form = ProfileForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            # last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            u=User.objects.get(username=user.username)
            u.first_name=first_name
            # u.last_name=last_name
            u.email=email
            u.save()
            # string='You have sucesfully updated your profile with \n\nFirst name: '+first_name+'\nLast_name: '+last_name+'\nEmail: '+email             
            # email1 = EmailMessage('SurveyTool', string, to=[email])
            # email1.send()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        #user_form = UserForm(instance=request.user)
        # user=request.user
        # u=User.objects.get(username=user.username)
        profile_form = ProfileForm
        # profile_form.first_name=u.first_name
        # profile_last.first_name=u.last_name
        # profile_form.first_name=u.first_name
        return render(request, 'updateprofile/updateprofile.html', {'profile_form': profile_form})

def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print "fff"
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/profile')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword/pass.html', {
        'form': form
}) 

def sample_view(request):
    current_user = request.user
    print current_user.username


def add_articles(request):
    if request.user.is_authenticated():
        return render(request,'articles/add_article.html')
    else:
        return HttpResponseRedirect('/login')


def shell(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('http://127.0.0.1:3000')
    else:
        return HttpResponseRedirect('/login')

def practice(request):
    questions=question.objects.all()
    print questions
    return render(request,'practice/practice.html',{'questions':questions})
def learn(request):
    return render(request,"learn/learn.html")
def reversing(request,id):
    articles=reversingarticle.objects.all()
    tag="learn/reversing/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})
def forensics(request,id):
    articles=forensicsarticle.objects.all()
    tag="learn/forensics/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})
def crypto(request,id):
    articles=cryptoarticle.objects.all()
    tag="learn/crypto/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})
def web(request,id):
    articles=webarticle.objects.all()
    tag="learn/web/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})
def binary(request,id):
    articles=binaryarticle.objects.all()
    tag="learn/binary/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})
def general(request,id):
    articles=generalarticle.objects.all()
    tag="learn/general/"
    tag+=id+".html"
    print tag
    return render(request,tag,{'articles':articles})



   