from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {
        'posts': posts
    })
