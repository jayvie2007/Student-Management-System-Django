from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import APIView
from .models import Student
# Create your views here.

#@APIView(['GET', 'POST'])
def index(request):
    return render(request, 'students/index.html',{
        'students': Student.objects.all()
        })
#the variable 'students' is used to call all the data inside the Student 
#model and hence to be called by loop inside the templates

def view_student(request, id):
    students = students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

