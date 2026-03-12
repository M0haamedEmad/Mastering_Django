from django.shortcuts import get_object_or_404, render
from .models import Post

# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post/detail.html', {'post': post})
