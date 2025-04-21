from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('account:login')
    else:
        return render(request, 'registration/register.html')
    
def profile(request):
    return render(request, 'registration/profile.html')