
from django.test import TestCase
from .models import Film, Director, Genre, Poster
from .serializers import FilmSerializer, DirectorSerializer, GenreSerializer, PosterSerializer
from django.utils import timezone
class SerializerTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(name='Christopher Nolan', year_of_birth=1970)
        self.genre = Genre.objects.create(name='Action')
        self.film = Film.objects.create(
            title='Inception',
            description='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
            year=2010,
            country='USA',
            director=self.director,
        )
        self.film.genre.add(self.genre)
        self.poster = Poster.objects.create(date='2023-03-09', films=self.film)

    def test_film_serializer(self):
        serializer = FilmSerializer(self.film)
        expected_data = {
            'id': self.film.id,
            'title': 'Inception',
            'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
            'year': 2010,
            'country': 'USA',
            'director': self.director.id,
            'genre': [self.genre.id],
            'posters': [self.poster.id]
        }
        self.assertEqual(serializer.data, expected_data)

    def test_director_serializer(self):
        serializer = DirectorSerializer(self.director)
        expected_data = {
            'id': self.director.id,
            'name': 'Christopher Nolan',
            'year_of_birth': 1970
        }
        self.assertEqual(serializer.data, expected_data)

    def test_genre_serializer(self):
        serializer = GenreSerializer(self.genre)
        expected_data = {
            'id': self.genre.id,
            'name': 'Action'
        }
        self.assertEqual(serializer.data, expected_data)

    def test_poster_serializer(self):
        serializer = PosterSerializer(self.poster)
        expected_data = {
            'id': self.poster.id,
            'date': '2023-03-09',
            'films': self.film.id
        }
        self.assertEqual(serializer.data, expected_data)




class ModelTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(name='Christopher Nolan', year_of_birth=1970)
        self.genre = Genre.objects.create(name='Action')
        self.film = Film.objects.create(
            title='Inception',
            description='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
            year=2010,
            country='USA',
            director=self.director,
        )
        self.film.genre.add(self.genre)
        self.poster = Poster.objects.create(date=timezone.now(), films=self.film)

    def test_film_str(self):
        self.assertEqual(str(self.film), 'Inception')

    def test_director_str(self):
        self.assertEqual(str(self.director), 'Christopher Nolan')

    def test_genre_str(self):
        self.assertEqual(str(self.genre), 'Action')

    def test_poster_str(self):
        self.assertEqual(str(self.poster), str(timezone.now().date()))

    def test_film_has_genre(self):
        self.assertIn(self.genre, self.film.genre.all())

    def test_film_has_director(self):
        self.assertEqual(self.director, self.film.director)

    def test_film_has_poster(self):
        self.assertIn(self.poster, self.film.posters.all())

    def test_poster_has_film(self):
        self.assertEqual(self.film, self.poster.films)
