from django.shortcuts import render
from django.http import HttpResponse
from UserModel.models import User
from ResourceClassModel.models import ResourceClass
from django.views.decorators import csrf

def login(request):
	user ={}
	list = ResourceClass.objects.all()
	user['list'] = list

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
				return HttpResponse("<script>alert('密码错误,请重新输入!');history.go(-1);</script>")
		except User.DoesNotExist:
			user['message'] = '账号或密码错误'
			return HttpResponse("<script>alert('账号或密码错误,请重新输入!');history.go(-1);</script>")
	return render(request, "login.html", user)

