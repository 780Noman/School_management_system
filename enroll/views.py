from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse # Import reverse
from django.urls import reverse_lazy # Import reverse_lazy
from .forms import StudentReg
from django.contrib import messages
from course.models import Course
from .models import Enrollment


def showformdata(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your registration has been successful! Please log in.')
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        fm = StudentReg()
    return render(request, 'enroll/userReg.html', context={'form': fm})


def studentinfo(request):
    stud = User.objects.all()
    return render(request, 'enroll/studetails.html', context={'stu': stud})


def enroll_course(request, course_id):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please register or log in to enroll in a course.')
        return HttpResponseRedirect(reverse('enroll:enroll')) # Redirect to registration page

    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        # Check if user is already enrolled
        if Enrollment.objects.filter(user=request.user, course=course).exists():
            messages.info(request, f'You are already enrolled in {course.name}.')
        else:
            Enrollment.objects.create(user=request.user, course=course)
            messages.success(request, f'Successfully enrolled in {course.name}!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) # Redirect back or to home
    
    # If not POST, render a confirmation page or redirect
    # For now, we'll just redirect back to the course detail page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def my_courses(request):
    enrolled_courses = Enrollment.objects.filter(user=request.user)
    return render(request, 'enroll/my_courses.html', {'enrolled_courses': enrolled_courses})