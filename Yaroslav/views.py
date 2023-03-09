from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Film, Director, Genre, Poster
from .serializers import FilmSerializer, DirectorSerializer, GenreSerializer, PosterSerializer



# Create your views here.

class FilmList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetail(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmCreate(CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class DirectorList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorCreate(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreCreate(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PosterList(ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterCreate(CreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer




