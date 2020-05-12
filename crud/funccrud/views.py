from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import NewPost
# Create your views here.

def welcome(request):
    return render(request, 'funccrud/index.html')

def read(request):
    posts = Post.objects.all()
    return render(request, 'funccrud/funccrud.html', {'posts':posts})

def create(request):
    # 새로운 게시물 저장 == POST
    # 작성 형식 띄어주기 == GET   
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewPost()
        return render(request, 'funccrud/new.html', {'form':form})

    return

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 객체 pk에 해당하는 입력공간
    form = NewPost(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'funccrud/new.html', {'form':form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')