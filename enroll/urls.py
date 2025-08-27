from django.urls import path
from . import views

app_name = 'enroll'

urlpatterns = [
    path('stu/',views.studentinfo),
    path('reg/',views.showformdata, name='enroll'),
    path('enroll_course/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('my_courses/', views.my_courses, name='my_courses'),
]