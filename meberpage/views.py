from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from members.models import Member
from .serializer import MemberSerializer
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.views.generic import View
from signup.forms import UserForm,UserLoginForm

def logout(request):
    if request.method=='POST':
        logout(request)
        return redirect('index:homepage')

class MemberList(APIView):

    def get(self,request):
        members=Member.objects.all()
        serializer=MemberSerializer(members,many=True)
        return Response(serializer.data)

    def post(self):
        pass





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
