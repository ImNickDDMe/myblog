from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UpdateUserDetails
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:profile')
        
        return super().dispatch(request, *args, **kwargs)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('account:login')
    else:
        if request.user.is_authenticated:
            return redirect('account:profile')

        return render(request, 'registration/register.html')
    
@login_required(login_url='/account/login')
def profile(request):
    if request.method == 'POST':
        form = UpdateUserDetails(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('account:profile')
        
        return render(request, 'registration/profile.html', {'form': form})
    else:
        form = UpdateUserDetails(instance=request.user)
        
        return render(request, 'registration/profile.html', {'form': form })