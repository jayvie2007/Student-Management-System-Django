from django.shortcuts import render
from .models import Student
from .serializers import Serializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import uuid

class getData(APIView):
    def get(self, request):
            students = Student.objects.all()
            serializers = Serializer(students, many=True)
            return Response({"Students": serializers.data})
    
class inputData(APIView):
      def post(self, request):
            students = Student.objects.get()
            student_number = generate_uid()
            request.data['student_number'] = student_number
            serializers = Serializer(students = request.data)
            if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data, status=status.HTTP_201_CREATED)

class deleteData(APIView):
      def delete(self, request, student_number):
            try:
                  students = Student.objects.get(student_number = student_number)
            except:
                  Student.DoesNotExist()
                  return Response(status=status.HTTP_404_NOT_FOUND)
            students.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
            
def generate_uid(self):
      student_number = uuid.uuid4().hex[-8:]
      return student_number
    


    