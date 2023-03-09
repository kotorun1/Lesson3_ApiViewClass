
from django.urls import path

from .views import FilmList, FilmDetail, FilmCreate, DirectorList, DirectorDetail, DirectorCreate, GenreList, GenreDetail, GenreCreate, PosterList, PosterDetail, PosterCreate


urlpatterns = [
    path('films/', FilmList.as_view()),
    path('films/<int:pk>/', FilmDetail.as_view()),
    path('films/create/', FilmCreate.as_view()),
    path('directors/', DirectorList.as_view()),
    path('directors/<int:pk>/', DirectorDetail.as_view()),
    path('directors/create/', DirectorCreate.as_view()),
    path('genres/', GenreList.as_view()),
    path('genres/<int:pk>/', GenreDetail.as_view()),
    path('genres/create/', GenreCreate.as_view()),
    path('posters/', PosterList.as_view()),
    path('posters/<int:pk>/', PosterDetail.as_view()),
    path('posters/create/', PosterCreate.as_view()),
]
