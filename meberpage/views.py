from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from members.models import Member
from .serializer import MemberSerializer

def homepage(request):
    return HttpResponse('homepage')

class MemberList(APIView):

    def get(self,request):
        members=Member.objects.all()
        serializer=MemberSerializer(members,many=True)
        return Response(serializer.data)

    def post(self):
        pass
