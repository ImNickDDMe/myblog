from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input input-lg'})
        self.fields['password1'].widget.attrs.update({'class': 'input input-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'input input-lg'})

    first_name = forms.CharField(
        max_length=40,
        label='Firstname',
        widget=forms.TextInput(attrs={'class': 'input input-lg'}),
        required=True
    )
    last_name = forms.CharField(
        max_length=40,
        label='Lastname',
        widget=forms.TextInput(attrs={'class': 'input input-lg'}),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'input input-lg'}),
        required=True
    )
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user
    
class UpdateUserDetails(forms.ModelForm):
    first_name = forms.CharField(
        max_length=40,
        label='Firstname',
        widget=forms.TextInput(attrs={'class': 'input input-lg'})
    )
    last_name = forms.CharField(
        max_length=40,
        label='Lastname',
        widget=forms.TextInput(attrs={'class': 'input input-lg'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input input-lg'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input input-lg', 'disabled': True})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user