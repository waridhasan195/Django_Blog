from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls.base import reverse
from ckeditor.fields import RichTextField



class Category(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    profile_pic = models.ImageField(null = True, blank = True, upload_to = 'images/profile_image/')
    website_url = models.CharField(max_length=250, null=True, blank=True)
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)
        
    def get_absolute_url(self):
        return reverse('home')


from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    featured = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title + '|' + (str(self.author))
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['-timestamp',]



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def total_comment(self):
        return self.name.count()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)