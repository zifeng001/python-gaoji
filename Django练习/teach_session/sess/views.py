from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.




# class StudentListView(ListView):
# 	queryset = Student.objects.all().filter(gender="man")
# 	template_name = "student_list.html"
#
#
#
# def mySess(request):
# 	print(type(request.session))
# 	print(request.session)
# 	print(request.session.get("teacher_name", "NoName"))
#
# 	request.session.clear()
# 	print('In mySess')
# 	return None
#
# def student(request):
#
# 	stus = Student.objects.all()
# 	# 2个参数
# 	# 1，数据来源，从数据库中查询出来
# 	# 2，单页返回数据量
# 	p = Paginator(stus,40)
# 	print(p.count)
# 	print(p.num_pages) # 页面总数
# 	return stus
