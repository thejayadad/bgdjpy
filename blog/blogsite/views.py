from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Post

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogsite/detail.html', {'post': post})