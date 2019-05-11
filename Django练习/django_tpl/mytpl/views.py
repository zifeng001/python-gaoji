from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
	return render(request,r"one.html")
def two(request):
	ct = dict()
	ct['name'] = '小鲫鱼'
	ct['name2'] = 'lalala'
	return render(request, r'two.html',context=ct)

def three(request):
	ct = dict()
	ct["score"] = [99,87,23,100,85,82]
	return render(request, r"three.html", context=ct)

def four(request):
	ct = dict()
	ct["name"] = "甲鱼"
	return render(request, r"four.html", context=ct)

def five_get(request):
	return render(request, r'five.html')

def five_post(request):
	print(request.POST)
	return render(request, r'one.html')