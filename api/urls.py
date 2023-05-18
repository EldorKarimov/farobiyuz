from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', CategoryAPIView.as_view()),
    path('course-list/', CourseListAPIView.as_view()),
    path('skill-list/', SkillListAPIView.as_view()),
    path('teacher-list/', TeacherListAPIView.as_view()),
    path('course-by-category/<slug:slug>/', CourseByCategory.as_view()),
    path('message/', MessageFromUserAPIView.as_view()),
    path('course/detail/<slug:slug>/', CourseDetailAPIView.as_view()),
]