from django.forms import ModelForm, TextInput, Select, CheckboxInput, PasswordInput
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
                'style': 'margin: 20%;',
            }),
            'user': Select(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 7%; margin: 20%;',
            }),
        }

class EditTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_completed']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin: 20%;',
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'width: 7%; margin: 20%;',
            }),
        }


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'password1': PasswordInput(attrs={
                'class': '',
                'style': 'width: 50%; margin-top: 5%',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 5%',
            }),
        }
