from django.db import models

class Item(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.IntegerField('Цена')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

class Image(models.Model):
    photos = models.ImageField('Фото', null=True, upload_to='photo_items/')
    items = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.photos

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'