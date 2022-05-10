from importlib import import_module
from operator import ipow
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from .forms import  Userform
from .models import User
from .serializers import StudentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView  


# Create your views here.


class cd(SuccessMessageMixin, FormView):
    form_class = Userform
    template_name = 'index.html'
    
    def form_valid(self,form):
        user= form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data['username']
        return username + '- User Created Successfully..!!'

class UserAPI(APIView):
    def get(self,request,pk=None,formate=None):
        id = pk
        if id is not None:
            stu = User.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = User.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,formate=None):
        serialilzer = StudentSerializer(data=request.data)
        if serialilzer.is_valid():
            serialilzer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return  Response(serialilzer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,formate = None):
        id = pk
        stu = User.objects.get(id=pk)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,formate = None):
        id = pk
        stu = User.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,formate=None):
        id = pk
        stu = User.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})



class InquiryAPI(APIView):
    def get(self,request,pk=None,formate=None):
        id = pk
        if id is not None:
            stu = User.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = User.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,formate=None):
        serialilzer = StudentSerializer(data=request.data)
        if serialilzer.is_valid():
            serialilzer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return  Response(serialilzer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,formate = None):
        id = pk
        stu = User.objects.get(id=pk)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,formate = None):
        id = pk
        stu = User.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,formate=None):
        id = pk
        stu = User.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


