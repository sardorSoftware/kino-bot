from django.db import models

class Movie(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.code} - {self.title}"
