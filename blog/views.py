from django.shortcuts import get_object_or_404, render, redirect
from .forms import EmailPostForm, CommentForm
from .models import Post, Comment

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

    comments = Comment.objects.filter(post_id=post.id)

    form = CommentForm()

    return render(request, 'post/post_details.html', { 
        'post': post,
        'comments': comments,
        'form': form 
    })

def post_share(request, post_slug):
    post = get_object_or_404(
            Post,
            slug=post_slug
        )

    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            pass
    else:
        form = EmailPostForm()

        return render(request, 'post/post_share.html', { 
            'form': form,
            'post': post
        })
    
def post_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            
            new_comment = Comment(
                post_id=post.id,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                body=form.cleaned_data['body']
            )
            new_comment.save()

            return redirect(post.get_absolute_url())
    else:
        return redirect(post.get_absolute_url())