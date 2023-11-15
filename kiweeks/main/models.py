from django.db import models


class Color_inside(models.Model):
    color = models.CharField('Цвет внутренний', max_length=100)
    code = models.CharField('Код цвета', max_length=8, default='000000')

    def __str__(self):
        return self.color

class Color_outside(models.Model):
    color = models.CharField('Цвет', max_length=100)
    code = models.CharField('Код цвета', max_length=8, default="000000")

    def __str__(self):
        return self.color


class Type_door(models.Model):
    type_doors = models.CharField('Тип двери', max_length=100)

    def __str__(self):
        return self.type_doors


class Category_door(models.Model):
    categories = models.CharField('Категория', max_length=255)
    urls = models.CharField('Ссылка на категории',max_length=255, null=True)

    def __str__(self):
        return self.categories

    class Meta:
        verbose_name = 'Тип двери'
        verbose_name_plural = 'Типы дверей'


class Size_door(models.Model):
    sizes_doors = models.CharField('Размер', max_length=25)

    def __str__(self):
        return self.sizes_doors

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Side_of_door(models.Model):
    sides = models.CharField('Сторона', max_length=15)

    def __str__(self):
        return self.sides

    class Meta:
        verbose_name = 'Сторона'
        verbose_name_plural = 'Стороны'


class Door(models.Model):
    title = models.CharField('Название', max_length=255)
    brand = models.CharField('Бренд', max_length=255)
    category_door = models.ForeignKey(Category_door, name='category', on_delete=models.CASCADE, null=True)
    type_doors = models.ForeignKey(Type_door, name='type', on_delete=models.CASCADE, null=True)
    sizes = models.ManyToManyField(Size_door, name='sizes', related_name='size_doors')
    sides = models.ManyToManyField(Side_of_door, name='sides', related_name='sides_of_doors')
    properties = models.TextField('Характеристики')
    description = models.TextField('Описание', null=True)
    colors_inside = models.ManyToManyField(Color_inside, related_name='color_inside')
    colors_outside = models.ManyToManyField(Color_outside, related_name='color_outside')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'


class Photo_door(models.Model):
    photos = models.ImageField('Фото', null=True, upload_to='photo_door/')
    doors = models.ForeignKey(Door, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

