from django.shortcuts import render
from django.http import HttpResponse
from ResourceClassModel.models import ResourceClass
from BlogModel.models import Blog
from django.views.decorators import csrf

def blog(request):
	context = {}
	if request.GET:
		id = request.GET.get('id')
		context['id'] = id
		try:
			blog = Blog.objects.get(id=context['id']);
			context['blog'] = blog
		except Blog.DoesNotExist:
			context['blog'] = 'error'
	list = ResourceClass.objects.all()
	context['list'] = list
	return render(request, "blog.html", context) 

