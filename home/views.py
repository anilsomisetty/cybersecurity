# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from models import *

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



def profile(request):
    #print request.user.id
    return render(request,'userdetails/profile.html')


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



   