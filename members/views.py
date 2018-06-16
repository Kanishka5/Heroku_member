from django.shortcuts import render
from .models import Member

def member(request):
    all_member=Member.objects.all()
    context={
        'all_member':all_member,
    }
    return render(request,'members/memberpage.html',context)
