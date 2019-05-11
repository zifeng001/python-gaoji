from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def teacher(r):
	return HttpResponse('这是teacher的一个视图')

def v2_exception(r):
	raise Http404
	return HttpResponse('ok')

def v10_1(request):
	return HttpResponseRedirect('/v11')

def v10_2(requeset):
	return HttpResponseRedirect(reverse('v11'))

def v8_get(request):
	rst = ''
	for k,v in request.GET.items():
		rst += k + '--->' +v
		rst += ','

	return HttpResponse('Get value of Request is {0}'.format(rst))

def v9_get(request):
	# 渲染模板并返回
	return render_to_response('for_post.html')

def v9_post(request):
	rst = ''
	for k,v in request.POST.items():
		rst += k + '--->' + v
		rst += ','
	return HttpResponse('Get value of POST is {0}'.format(rst))

def v11(requeset):
	return HttpResponse('这个是v11的访问返回哈')

def render_test(request):
	# 环境变量
	c = dict()
	rsp = render(request, 'render.html')
	return rsp

def render2_test(request):
	# 环境变量
	c = dict()
	c['name'] = 'xiaojiayu'
	rsp = render(request, 'render2.html', context=c)
	return rsp

def render3_test(request):
	from django.template import loader
	# 得到模板
	t = loader.get_template('render2.html')
	print(type(t))
	r = t.render({'name':'are you ok? '})
	print(type(r))
	return HttpResponse(r)

def render4_test(request):
	# 反馈回模板render
	rsp = render_to_response('render2.html', context={'name':'are you'})
	return rsp