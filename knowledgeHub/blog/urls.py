from blog import views
from django.urls import path 
from .views import HomeListView, PostDetailView, CreatePostView, UpdatepostView, DeletePostView, AddCategoryView, CategoryWiseView, CategoryListView, search, AddCommentView, LikeView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('add-post/', CreatePostView.as_view(), name = 'add-post'),
    path('update-post/<int:pk>/', UpdatepostView.as_view(), name = 'update-post'),
    path('delete-post/<int:pk>/', DeletePostView.as_view(), name = 'delete-post'),
    path('add-category/', AddCategoryView.as_view(), name = 'add-category'),
    path('category/<int:pk>/', CategoryWiseView, name = 'category'),
    path('category-list/', CategoryListView.as_view(), name = 'category-list'),
    path('search/', search, name = 'search'),
    path('post-detail/<int:pk>/comment/', AddCommentView.as_view(), name = 'add-comment'),
    path('like/<int:pk>/', LikeView, name = 'like_post'),

]