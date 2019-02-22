from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    # a = Movie.objects.filter(title='title')
    movies = Movie.objects.all()
    return render(request, 'index.html',{'movies': movies})

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'detail.html',{'movie': movie})
    
def delete(request, pk):
    d_movie = Movie.objects.get(pk=pk)
    d_movie.delete()
    return redirect('/movies/')
    
def edit(request, pk):
    u_movie = Movie.objects.get(pk=pk)
    return render(request, 'edit.html', {'u_movie': u_movie})
    
def update(request, pk):
    u_movie = Movie.objects.get(pk=pk)
    u_movie.title = request.POST.get('title')
    u_movie.audience = request.POST.get('audience')
    u_movie.genre = request.POST.get('genre')
    u_movie.score = request.POST.get('score')
    u_movie.poster_url = request.POST.get('poster_url')
    u_movie.description = request.POST.get('description')
    # u_movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    u_movie.save()
    return redirect('/movies/')