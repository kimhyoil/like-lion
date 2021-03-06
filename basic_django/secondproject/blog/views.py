from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects    # 쿼리셋(모델로 부터 전달받은 객체목록)
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    print(page)
    posts = paginator.get_page(page)
    print(posts)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})
    # 쿼리셋과 메소드 형식
    # 모델.쿼리셋s

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'detail':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    elif request.method == 'GET':
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
    else:
        print("error")
