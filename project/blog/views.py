from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .form import Blogform
from .models import Blog

def index(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
	#request된 페이지를 얻어온 뒤 return 해 준다
    blogs = paginator.get_page(page)

    return render(request, 'index.html', {'blogs':blogs, 'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request): 
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.date = timezone.now()
            blog.save()
            return redirect('detail', blog_id=blog.pk)
    else :
        form = Blogform()
        
    return render(request, 'new.html', {'form' : form})     


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  
    return redirect('blog/'+str(blog.id)) 

def modify(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    if request.method == 'POST':
        form = Blogform(request.POST, instance = blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.date = timezone.now()
            blog.save()
            return redirect('detail', blog_id = blog.pk)
    else:
        form = Blogform(instance = blog)
    return render(request, 'modify.html', {'form':form, 'blog_id':blog.pk})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('index')