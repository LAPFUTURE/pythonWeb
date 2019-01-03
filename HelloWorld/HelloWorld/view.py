from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from TestModel.models import Test
from UserModel.models import User
from BlogModel.models import Blog
from django.http import JsonResponse
from ResourceClassModel.models import ResourceClass

from django.conf import settings
import sys
sys.path.append(r"D:\Coding\1\fengge\xiangmu\xiangmu\HelloWorld\ceshi")
 
import eval

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

def handlepicture(request):
    # print(request.FILES['image'])
    # arr = [request.POST['styles']+'.ckpt-done',request.FILES['image']]
    f1 = request.FILES['image']
    fname = '%s/%s' % (settings.MEDIA_ROOT, f1.name)
    picname = fname.split(".")[0]+".jpg"
    with open(picname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    print("picture OK",picname)

    post_pic = str(picname.split("/")[3])

    arr = [request.POST['styles']+'.ckpt-done','../HelloWorld/ceshi/generated/'+post_pic]
    # eval.main(arr)
    obj = {"url":'../HelloWorld/ceshi/generated/res.jpg',"post":request.POST['styles'],"post_pic":post_pic,"picname":picname}
    # obj = {"url":'../HelloWorld/ceshi/generated/'+post_pic,"post":request.POST['styles'],"post_pic":post_pic,"picname":picname}

    return JsonResponse(obj)

