from django.db import models
from filer.fields.image import FilerImageField


class IndexModel(models.Model):
    pass


class SlideImg(models.Model):
    img = FilerImageField(null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Добавить фотографии в карусель'
        ordering = ['img']

    def __str__(self):
        return f'{self.img}'