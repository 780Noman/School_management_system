from django.shortcuts import render
from course.models import Course # Import the Course model

# Create your views here.
def home(request):
    # Fetch a few top courses (e.g., the first 3)
    top_courses = Course.objects.all().order_by('id')[:3]
    return render(request,'core/home.html',context={'top_courses': top_courses})

def about(request):
    return render(request, 'core/about.html')