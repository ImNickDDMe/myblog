from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post/post_list.html', {'posts': posts })

def post_details(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    return render(request, 'post/post_details.html', {'post': post })