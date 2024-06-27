from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }

    return render(request, "movies/home.html", context)

def detail(request, movie_id):
    movie = get_object_or_404(Post, id=movie_id)
    
    print(movie)

    if(isinstance(movie, Post)):
        title = movie.title
    else:
        title = "404"

    context = {
        "movie": movie,
        "title": title
    }

    return render(request, "movies/detail.html", context)