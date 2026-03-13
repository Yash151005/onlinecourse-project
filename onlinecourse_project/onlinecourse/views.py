from django.shortcuts import render
from .models import Course

def course_details(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

def submit(request):
    return render(request, 'onlinecourse/result.html')

def show_exam_result(request):
    return render(request, 'onlinecourse/result.html')