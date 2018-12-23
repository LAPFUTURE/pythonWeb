from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from TestModel.models import Test
from UserModel.models import User

def index(request):
	return render_to_response('index.html')

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['name'] = "lap"
    context['age'] = 21
    context['script'] = '<script>alert(123);</script>'
    return render(request, 'hello.html', context)

# def login(request):
# 	test1 = User(number='123@qq.com',password='123456')
# 	test1.save()

# 	context = {}
# 	context['request_path'] = request.path
# 	if context['request_path'] == '/login':
# 		context['error_message'] = 'yes'
# 	else:
# 		context['error_message'] = 'no'
# 	return render(request,'login.html',context)

def register(request):
	return render_to_response('register.html')

