from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

all_posts = [
    {
        'slug' : 'hike-in-the-mountains',
        'image': 'mountain.jpg',
        'author': 'Jarin',
        'date': date(2023,9,30),
        'title': 'Hike in the mountains',
        'excerpt': 'Alice and Bob, two friends, set out for a hike in the mountains on a clear summer day.',
        'content': '''Alice and Bob, two friends, set out for a hike in the mountains on a clear summer day.

They followed a winding trail through lush forests and meadows, their footsteps muffled by the soft earth beneath them. The air was crisp and clean, and the only sounds were the chirping of birds and the gentle rustling of leaves in the breeze.

As they hiked, Alice and Bob marveled at the beauty of the natural world around them. They spotted wildflowers blooming in the meadows and listened to the birdsong echoing through the trees. They crossed crystal-clear streams and climbed rocky outcrops, their senses heightened by the peace and solitude of the mountains.

After a few hours of hiking, Alice and Bob reached a breathtaking viewpoint. They paused to catch their breath and admire the stunning panorama of snow-capped peaks and valleys stretching out before them. In the distance, they could see a waterfall cascading down a mountainside.

Alice and Bob sat down on a rock and savored the moment. They felt grateful for the opportunity to experience the beauty of nature and to share this special day together. As the sun began to set, they slowly made their way back down the trail, tired but fulfilled.

The hike was a reminder of the simple pleasures in life and the importance of appreciating the beauty of nature. It was also a testament to the power of friendship and the shared experiences that create lasting memories.
        '''
    },
    {
        'slug' : 'into-the-wood',
        'image': 'woods.jpg',
        'author': 'Pepik',
        'date': date(2023,4,10),
        'title': 'Into the wood',
        'excerpt': 'Two friends set out for a hike into the woods on a sunny fall day. They followed a narrow path that wound through the trees, their footsteps crunching on the fallen leaves.',
        'content': '''The air was crisp and cool, and the only sounds were the rustle of leaves in the breeze and the occasional chirp of a bird.

As they hiked, the friends marveled at the beauty of the autumn forest. The trees were ablaze with color, their leaves turning shades of red, orange, and yellow. The underbrush was dotted with wildflowers, and the air was filled with the sweet scent of decaying leaves.

After a few hours of hiking, the friends reached a clearing in the woods. They sat down on a fallen log and took in the view. In the center of the clearing was a small pond, its surface reflecting the trees and sky above.

The friends spent the rest of the afternoon enjoying the peace and solitude of the woods. They talked and laughed, and shared stories of their lives. They watched as the sun slowly sank below the horizon, casting a golden glow over the clearing.

As the day came to a close, the friends reluctantly began the hike back to their car. They felt grateful for the opportunity to experience the beauty of nature and to share this special day together. The hike was a reminder of the simple pleasures in life and the importance of appreciating the beauty of the natural world.
        '''
    },
    {
        'slug' : 'programming',
        'image': 'coding.jpg',
        'author': 'Jose',
        'date': date(2023,10,1),
        'title': 'Programming',
        'excerpt': 'Programming is the process of creating instructions for a computer to follow.',
        'content': '''It is a powerful tool that can be used to solve a wide variety of problems, from simple tasks like calculating the sum of two numbers to complex tasks like developing artificial intelligence systems.

To learn to program, you need to learn a programming language. A programming language is a way of communicating with a computer. It is a set of rules and symbols that define how to write instructions for the computer to follow.

There are many different programming languages out there, each with its own strengths and weaknesses. Some popular programming languages include Python, Java, C++, JavaScript, and C#.

Once you have chosen a programming language, you need to learn how to use it. You can do this by reading books, articles, and tutorials. You can also take online courses or workshops.

Once you have learned the basics of programming, you can start writing your own programs. You can start with simple programs, such as a program to print "Hello, world!" to the console. As you get more experienced, you can write more complex programs, such as a program to play a game or to solve a mathematical problem.
        '''
    },
    {
        'slug' : 'broken-car',
        'image': 'car.jpg',
        'author': 'Alice',
        'date': date(2022,10,1),
        'title': 'Broken car',
        'excerpt': 'A broken car can be a frustrating experience, but it doesnt have to be. Here are a few tips on what to do if your car breaks down',
        'content': '''

    Stay calm. It's important to stay calm and assess the situation. If you're on a busy road, pull over to a safe location and turn on your hazard lights.
    Check for injuries. If you or anyone else has been injured, call 911 immediately.
    Call for help. If your car is not drivable, you will need to call for help. You can call a tow truck, a roadside assistance service, or a friend or family member.
    Exchange information. If you are in an accident, exchange information with the other driver(s), including insurance information.
    Document the damage. Take pictures of the damage to your car and the other vehicle(s) involved in the accident. This will help your insurance company to process your claim.

        '''
    },
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
    latest_posts = sorted(all_posts, key=get_date)[-3:]
    return render(request, 'blog/index.html',{
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })