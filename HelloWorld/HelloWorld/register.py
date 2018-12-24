from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from ResourceClassModel.models import ResourceClass
from UserModel.models import User

def register(request):
	newUser = {}
	list = ResourceClass.objects.all()
	newUser['list'] = list
	if request.POST:
		try:
			status = User.objects.get(number=request.POST['newnumber'])
			return HttpResponse("<script>alert('此账号已被注册!');history.go(-1);</script>")
		except User.DoesNotExist:
			newUser['number'] = request.POST['newnumber']
			newUser['password'] = request.POST['password']
			test1 = User(number=newUser['number'],password=newUser['password'])
			test1.save()
			return HttpResponse("<script>alert('注册成功!前往登录');window.location.href='/login';</script>")
	return render(request, "register.html", newUser)