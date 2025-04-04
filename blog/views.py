from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return redirect('/posts')

def posts(request):
    return render(request, 'posts.html')