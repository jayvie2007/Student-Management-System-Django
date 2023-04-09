from django.shortcuts import render
from .models import Student
from .serializers import Serializer

from rest_framework.response import Response
from rest_framework.views import APIView

class getData(APIView):
    def get(self, request):
            students = Student.objects.all()
            serializers = Serializer(students, many=True)
            return Response({"Students": serializers.data})
    
class inputData(APIView):
      def post(self, request):
            students = Student.objects.get()
            serializers = Serializer(students = request.data)
            if serializers.is_valid():
                  serializers.save()
                  return Response(serializers.data)
    


    