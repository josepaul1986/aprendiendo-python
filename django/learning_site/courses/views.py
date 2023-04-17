from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.
def courses(request):
    ## courses = Course.objects.all()
    ## course_list = "- ".join([str(course.name) for course in courses])
    ## return HttpResponse(course_list)
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', { 'courses': courses })
