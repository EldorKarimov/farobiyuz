from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from farobiy.models import *

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CourseListAPIView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class SkillListAPIView(APIView):
    def get(self, request):
        skills = Skils.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class TeacherListAPIView(APIView):
    def get(self, request):
        teachers = Teachers.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class CourseByCategory(APIView):
    def get(self, request, **kwargs):
        slug = kwargs['slug']
        category = Category.objects.get(slug = slug)
        courses = Courses.objects.filter(category__name = category.name)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class MessageFromUserAPIView(APIView):
    def post(self, request):

        serializer = MessageFromUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailAPIView(APIView):
    def get(self, request, **kwargs):
        slug = kwargs.get('slug')
        course = Courses.objects.get(slug = slug)
        serializer = CourseSerializer(course)

        return Response(serializer.data)