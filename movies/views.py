from django.shortcuts import render
from .models import Moviedata
from rest_framework import viewsets
from .serializers import MovieSerializer
from django.core.paginator import Paginator
# Create your views here.


class MovieView(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ComedyView(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy/animation')
    serializer_class = MovieSerializer


def Movie(request):
    movie_objects = Moviedata.objects.all()

    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movie_objects = Moviedata.objects.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objects, 2)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)

    return render(request, 'movies/index.html', {'movie_objects': movie_objects})
