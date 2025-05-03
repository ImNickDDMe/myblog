from .models import Comment
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        label='Your name',
        widget=forms.TextInput(attrs={'class': 'input input-lg'})
    )
    email = forms.EmailField(
        label='Your email',
        widget=forms.EmailInput(attrs={'class': 'input input-lg'})
    )
    to = forms.EmailField(
        label='Receipient\'s email',
        widget=forms.EmailInput(attrs={'class': 'input input-lg'})
    )
    comments = forms.CharField(
        required=False,
        label='Comments', 
        widget=forms.Textarea(attrs={'class': 'textarea textarea-md'})
    )

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=25,
        label='Your name',
        widget=forms.TextInput(attrs={'class': 'input input-lg'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input input-lg'})
    )
    body = forms.CharField(
        required=True, 
        widget=forms.Textarea(attrs={'class': 'textarea textarea-md'})
    )

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']