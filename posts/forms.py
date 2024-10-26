from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'description']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description', 'url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }