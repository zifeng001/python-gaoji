from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.

class StudentVS(viewsets.ModelViewSet):
	pass

class StudentAPIView(APIView):
	'''
	处理用户的get请求
	'''
	def get(self, request):
		print("in APIView get")
		return None