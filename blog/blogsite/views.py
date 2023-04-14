from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Post
from .forms import CommentForm

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'form': form})
