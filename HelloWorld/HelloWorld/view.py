from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from TestModel.models import Test
from UserModel.models import User
from BlogModel.models import Blog
from ResourceClassModel.models import ResourceClass


def index(request):
    context = {}
    list = ResourceClass.objects.all()
    context['list'] = list

    vueBlogs = Blog.objects.filter(categoryId=1)
    context['vueBlogs'] = vueBlogs

    reactBlogs = Blog.objects.filter(categoryId=2)
    context['reactBlogs'] = reactBlogs

    phpBlogs = Blog.objects.filter(categoryId=3)
    context['phpBlogs'] = phpBlogs

    javaBlogs = Blog.objects.filter(categoryId=4)
    context['javaBlogs'] = javaBlogs

    pythonBlogs = Blog.objects.filter(categoryId=5)
    context['pythonBlogs'] = pythonBlogs

    books = Blog.objects.filter(categoryId=6)
    context['books'] = books

    return render(request, 'index.html', context)

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['name'] = "lap"
    context['age'] = 21
    context['script'] = '<script>alert(123);</script>'
    return render(request, 'hello.html', context)

def download(request):
    response = {}
    if request.GET:
        id = request.GET.get('id')
        response['id'] = id
    return response

