from django.shortcuts import render
from api.models import Course
from rest_framework.response import Response
from api.serializers import CourseSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
class Course_list(APIView):
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class Course_detail(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Http404
    
    def get(self,request,pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def post(self,request,pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)