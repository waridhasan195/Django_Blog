
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Profile, Comment
from .forms import CreatePost, UpdatePost, CommentForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Count, Q, query
from django.db.models.lookups import IContains
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
        liked = False
    return HttpResponseRedirect(reverse( 'post-detail', args=[str(pk)]))


class HomeListView(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        latest_post = Post.objects.order_by('-timestamp')[0:3]
        post_list = Post.objects.all()
        comment = Comment.objects.all()
        
        paginator = Paginator(post_list, 5)
        page_request_var = 'page'
        page = self.request.GET.get(page_request_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)

        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        context["latest_post"] = latest_post
        context["queryset"] = paginated_queryset
        context["comment"] = comment
        context["page_request_var"] = page_request_var
        

        return context


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        latest_post = Post.objects.order_by('-timestamp')[0:3]
        category_count = get_category_count()
        num_visits = self.request.session.get('num_visits', 1)
        self.request.session['num_visits'] = num_visits + 1
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        post_view = get_object_or_404(Post, id=self.kwargs['pk'])
        post_view.view_count = post_view.view_count + 1
        post_view.save()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        total_likes = stuff.total_likes()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["latest_post"] = latest_post
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["category_count"] = category_count
        context["num_visits"] = num_visits
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')

class UpdatepostView(UpdateView):
    model = Post 
    form_class = UpdatePost
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class CategoryList(ListView):
    model = Category
    template_name = 'header.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


def CategoryWiseView(request, pk):
    category_list_object = Post.objects.filter(categories = pk)
    paginator = Paginator(category_list_object, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset':paginated_queryset,
        'page_request_var':page_request_var,
        'category_list_object':category_list_object,
    }
    print(paginator)
    return render(request, 'Category_View_post.html', context)


def search(request):
    quertset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        quertset = quertset.filter(
            Q(title__icontains = query)
        ).distinct()
    context = {
        'queryset':quertset
    }
    return render(request, 'search_results.html', context)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
