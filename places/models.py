from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.order} {self.title}'
