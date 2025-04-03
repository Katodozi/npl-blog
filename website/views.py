from django.shortcuts import render
from .models import Club, Player, BlogPost

def home(request):
    clubs_list = Club.objects.all()
    latest_posts = BlogPost.objects.order_by('-created_at')[:3]
    return render(request, 'website/home.html', {'clubs': clubs_list, 'latest_posts': latest_posts})

def clubs(request):
    clubs_list = Club.objects.all()
    return render(request, 'website/clubs.html', {'clubs': clubs_list})

def players(request, club_id):
    players_list = Player.objects.filter(club_id=club_id)
    return render(request, 'website/players.html', {'players': players_list})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'website/blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'website/post_detail.html', {'post': post})
