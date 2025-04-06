from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'post/post_list.html')

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'posts/post_details.html', {'post': post})