from django import forms
from .models import Post

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'body']