from django.http import HttpResponse

# Create your views here.
def posts(request):
    return HttpResponse('Posts')