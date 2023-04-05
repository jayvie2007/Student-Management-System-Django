from django.shortcuts import render
from rest_framework.decorators import APIView
# Create your views here.

#@APIView(['GET', 'POST'])
def index(request):
    return render(request, 'students/index.html')
