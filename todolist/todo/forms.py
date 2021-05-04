from django import forms
from .models import ToDo

class ToDoList(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo']
        widgets = {
            'todo': forms.TextInput(
                attrs={
                    'placeholder': 'write todo', 
            }),
        }
