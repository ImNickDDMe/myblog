from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib import admin
from django.urls import reverse
from .models import Post
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        super().clean()

        banned_words = [
            'dumbass', 
            'loser', 
            'Loser', 
            'Dumbass', 
            'stupid', 
            'Stupid'
        ]
            
        for word in banned_words:
            if self.cleaned_data['title'] in word:
                raise forms.ValidationError("Prohibited words in title.")

        return self.cleaned_data

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'view_author')
    list_filter = ('publish', 'status')
    search_fields = ['title']

    form = PostAdminForm

    def view_author(self, obj):
        url = (
            reverse('admin:auth_user_changelist')
            + '?'
            + urlencode({'user__id': f'{obj.id}'})
        )

        return format_html('<a href="{}">{}</a>', url, obj.author)

    view_author.short_description = 'Author'