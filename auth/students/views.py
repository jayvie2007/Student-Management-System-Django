from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm
# Create your views here.

def index(request):
    return render(request, 'students/index.html',{
        'students': Student.objects.all()
        })
#the variable 'students' is used to call all the data inside the Student 
#model and hence to be called by loop inside the templates

def view_student(request, id):
    students = students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'GET':
        # Render the add student form template
        return render(request, 'students/add.html')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_course = form.cleaned_data['course']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                course = new_course,
                gpa = new_gpa,
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success':True,
            })
        else:
            form = StudentForm()
        return render(request, 'students/add.html',{
        'form': StudentForm()
        })
