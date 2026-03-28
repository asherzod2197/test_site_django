from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Quiz, Category


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Foydalanuvchi nomi',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol',
        })
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Foydalanuvchi nomi',
        })
    )
    password1 = forms.CharField(
        label='Parol',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol',
        })
    )
    password2 = forms.CharField(
        label='Parolni tasdiqlang',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parolni qayta kiriting',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class QuizForm(forms.ModelForm):
    markdown_content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 20,
            'placeholder': 'Markdown formatida savollarni yozing...',
        }),
        label='Markdown kontent'
    )
    markdown_upload = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.md'}),
        label='.md fayl yuklash'
    )

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'difficulty']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test sarlavhasi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Test tavsifi'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategoriya nomi'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'url-slug'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qisqa tavsif'}),
        }
