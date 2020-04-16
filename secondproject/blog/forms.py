from django import forms
from .models import Blog

# 모델을 기반으로한 form
class BlogPost(forms.ModelForm):
    class Meta: 
        model = Blog 
        fields = ['title', 'body']

# 모델을 기반으로 하지 않은 form
# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=100)
#     max_number = forms.ChoiceField(choices=[('1','one'), ('2', 'two')])
