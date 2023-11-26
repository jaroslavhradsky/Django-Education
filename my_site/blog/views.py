from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3] # Descending order, first three
    #latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'blog/index.html',{
        'posts': latest_posts,
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')

    return render(request, 'blog/posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    #identified_post = next(post for post in all_posts if post['slug'] == slug)
    #identified_post = Post.objects.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags' : identified_post.tags.all()
    })