from django.db import models


class Place(models.Model):
    title = models.CharField('название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Полное описание')
    latitude = models.FloatField('широта', blank=True)
    longitude = models.FloatField('долгота', blank=True)

    def __str__(self):
        return self.title

    def get_images_paths(self):
        paths = []
        if self.images:
            for image in self.images.all():
                paths.append(image.image.url)
        return paths


class Image(models.Model):
    title = models.CharField('название', max_length=200)
    order = models.PositiveIntegerField('порядок', )
    image = models.ImageField('изображение', upload_to='images')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.order} {self.title}'
