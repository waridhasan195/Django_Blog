from django.shortcuts import render
from django.views import generic
from blog.models import Profile
from django.views.generic import DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .forms import ProfilePageForm, EditProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'create_user_profile_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        
class EditProfilePageView(UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'edit_profile_page.html'
    success_url = reverse_lazy('home')



class UserProfileSettingView(UpdateView):
    form_class = EditProfileForm
    template_name = 'profile_setting.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

