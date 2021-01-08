from django import forms
from django.forms import fields
from .models import Post, Comment


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'thumbnail', 'categories', 'previous_post', 'next_post']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','id': 'username', 'value': '', 'type': 'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'previous_post': forms.Select(attrs={'class': 'form-control'}),
            'next_post': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail', 'previous_post', 'next_post']
    
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'previous_post': forms.Select(attrs={'class': 'form-control'}),
            'next_post': forms.Select(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','id': 'username', 'value': '', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }