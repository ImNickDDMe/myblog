from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    publish = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unique__for_date = 'publish'

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'P', 'Published'
   
    status = models.CharField(max_length=20, choices=Status, default=Status.DRAFT)

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='idx_post_title')    
        ]

        ordering = ['publish']

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('blog:post_details', kwargs={
            'day': self.publish.day,
            'month': self.publish.month,
            'year': self.publish.year,
            'post_slug': self.slug
        })