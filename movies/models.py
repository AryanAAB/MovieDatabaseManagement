from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 500)
    director = models.CharField(max_length = 500)
    release_date = models.DateField()
    genre = models.CharField(max_length = 500)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)

    def __str__(self):
        return self.title