from django.db import models

class Movie(models.Model):
    code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    file_id = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
