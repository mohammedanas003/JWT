from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users,Teacher
from .serializers import Teacher_serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
 
class RegistrationAPI(APIView):
    def post(self,request):
        nm=request.data["username"]
        ph=request.data["phonenumber"]
        em=request.data["email"]
        pw=request.data["password"]
        cpw=request.data["cpassword"]
        if pw==cpw:
          if Users.objects.filter(email=em).exists():
             return Response("emailId exists")
          if Users.objects.filter(ph_no=ph).exists():
             return Response("phone number already exists")
          else:
           register=Users(username=nm,ph_no=ph,email=em)
           register.set_password(pw)
           register.save()
           return Response("user registered")
        else:
           return Response("password does not match")


class TeacherAPI(ModelViewSet):
   
   permission_classes=[IsAuthenticated]
   
   queryset=Teacher.objects.all()
   serializer_class=Teacher_serializers


