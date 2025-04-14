from django.shortcuts import get_object_or_404, render
from .forms import EmailPostForm, CommentForm
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post/post_list.html', { 'posts': posts })

def post_details(request, year, month, day, post_slug):
    post = get_object_or_404(
        Post, 
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post_slug
    )

    return render(request, 'post/post_details.html', { 'post': post })

def post_share(request):
    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            pass
    else:
        form = EmailPostForm()

        post_slug = request.GET['post']

        post = get_object_or_404(
            Post,
            slug=post_slug
        )

        return render(request, 'post/post_share.html', { 
            'form': form,
            'post': post
        })
    
def post_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            pass
    else:
        pass