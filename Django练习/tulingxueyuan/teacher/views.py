from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
视图函数需要一个参数，类型 应该是HttpResquest
'''
def do_normalmap(request):
	print("In do normalmap")
	return HttpResponse("This is normalmap")

def withparam(request,year,month):
	return HttpResponse('This is with param{0},{1}'.format(year, month))

def do_app(requset):
	return HttpResponse('这是个子路由')

def do_param2(requset,pn):
	return HttpResponse('This is book{0}'.format(pn))

def extremParam(r, name):
	return HttpResponse('my name is {0}'.format(name))










