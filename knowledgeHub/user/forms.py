
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from blog.models import Profile
from django.contrib.auth.forms import UserChangeForm


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'youtube_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditProfileForm(UserChangeForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')
