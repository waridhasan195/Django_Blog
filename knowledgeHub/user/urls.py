
from django.urls import path 
from .views import ShowProfilePageView, CreateProfilePageView, EditProfilePageView, UserProfileSettingView
urlpatterns = [
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name = 'create_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name = 'edit_profile_page'),
    path('profile_setting/', UserProfileSettingView.as_view(), name = 'profile_setting'),

]