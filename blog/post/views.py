from django.shortcuts import render, get_object_or_404
from. models import Post 
# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html', {'posts': posts})

def post_details(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})
