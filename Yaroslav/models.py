from django.db import models

class Poster(models.Model):
    date = models.DateField()
    films = models.ForeignKey('Film', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
   
    
class Film(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.IntegerField()
    country = models.CharField(max_length=50)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    posters = models.ManyToManyField(Poster, blank=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()    

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
