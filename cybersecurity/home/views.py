# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request,'index_authenticated.html')
    else:
        return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})


def sample_view(request):
    current_user = request.user
    print current_user.username


def add_articles(request):
    return render(request,'articles/add_article.html')
