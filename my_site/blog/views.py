from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Post

from datetime import date

obsolete_posts = [
    {
    'slug' : 'python-snake',
    'image': 'python.jpg',
    'author': 'Anonymous',
    'date': date(2000,10,1),
    'title': 'Python Snake: A Gentle Giant',
    'excerpt': 'The python snake is a member of the family Pythonidae, which contains the largest snakes in the world. ',
    'content': '''
        There are over 30 species of pythons, found in Africa, Asia, and Australia. Pythons are non-venomous snakes, and they are known for their gentle nature.

        Pythons are constrictors, meaning they kill their prey by wrapping their bodies around them and squeezing until they suffocate. Pythons typically eat mammals, birds, and reptiles. They are ambush predators, waiting for their prey to come within reach before striking.

        Pythons are important predators in their ecosystems. They help to control populations of rodents and other small animals. Pythons are also a food source for other animals, such as crocodiles, jaguars, and eagles.

        Pythons are popular pets, but they are not for everyone. Pythons can grow to be very large, and they require a lot of care. It is important to do your research before getting a python pet.
        '''
    }
]

def get_date(post):
    return post['date']


# Create your views here.


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date', 'author']
    context_object_name = 'posts'

    def get_queryset(self):
        query_set =  super().get_queryset()
        data = query_set[:3]
        return data

''' BEFORE CLASS VIEWS
def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3] # Descending order, first three
    #latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'blog/index.html',{
        'posts': latest_posts,
    })
'''

class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    ordering = ['-date', 'author']
    context_object_name = 'all_posts'


''' BEFORE CLASS VIEWS
def posts(request):
    all_posts = Post.objects.all().order_by('-date')

    return render(request, 'blog/posts.html', {
        'all_posts': all_posts
    })
'''

class SinglePostView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context


''' BEFORE CLASS VIEWS
def post_detail(request, slug):
    #identified_post = next(post for post in all_posts if post['slug'] == slug)
    #identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags' : identified_post.tags.all()
    })
'''