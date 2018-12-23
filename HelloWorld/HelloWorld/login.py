from django.shortcuts import render
from django.http import HttpResponse
from UserModel.models import User
from django.views.decorators import csrf
# from BaseException import DoesNotExist
 
# 接收POST请求数据
def login(request):
    user ={}
    if request.POST:
    	user['number'] = request.POST['number']
    	user['password'] = request.POST['password']
    	try:
    		status = User.objects.get(number=user['number'])
    		if status.password == user['password']:
    			user['message'] = '<script>alert("登录成功")</script>'
    			return HttpResponse("<script>alert('登录成功!');window.location.href='/index';</script>")
    		else:
    			user['message'] = '密码错误!'
    			return HttpResponse("<script>alert('密码错误,请重新输入!');window.location.href='/login';</script>")	
    	except User.DoesNotExist:
    		user['message'] = '账号或密码错误'
    		return HttpResponse("<script>alert('账号或密码错误,请重新输入!');window.location.href='/login';</script>")	
    return render(request, "login.html", user)

