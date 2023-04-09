from django.forms import ModelForm, TextInput, Textarea
from .models import Todo, TodoItems
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'color: coral; width: 50%;',
            }),
        }
        
class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'color: coral; width: 50%;',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'style': 'color: coral; width: 50%;',
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'style': 'color: coral; width: 50%;',
            }),
        }
