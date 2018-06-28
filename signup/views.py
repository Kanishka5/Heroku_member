# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.views.generic import View
from .forms import UserForm,UserLoginForm


def login_view(request):
    if request.method=='POST':
        title="Login"
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        form=UserLoginForm()
    return render(request,'signup/login.html',{'form':form})



def register_view(request):
    if request.method == 'POST':
        title="Register"
        form=UserForm(request.POST)
        if form.is_valid():

            user=form.save(commit=False)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form=UserForm()
        context={
            'form':form,
            }
    return render(request,"signup/signup.html",context)
