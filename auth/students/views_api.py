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
            student_number = generate_uid()
            serializers = Serializer(data = request.data)
            request.data._mutable = True
            request.data['student_number'] = student_number
            request.data._mutable = False
            if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteData(APIView):
      def delete(self, request, student_number):
            try:
                  students = Student.objects.get(student_number = student_number)
            except Student.DoesNotExist():
                  return Response(status=status.HTTP_404_NOT_FOUND)
            students.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      
class editData(APIView):
      def put(self,request,student_number):
            try:
                  students = Student.objects.get(student_number = student_number)
                  firstname = request.data['first_name']
                  lastname =  request.data['last_name']
                  email = request.data['email']
                  course = request.data['course']
                  gpa = request.data['gpa']
            except Student.DoesNotExist():
                  return Response(status=status.HTTP_404_NOT_FOUND)
            serializers = Serializer(students, data = request.data)
            if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_uid():
      student_number = uuid.uuid4().hex[-8:]
      return student_number
    


    