from django.shortcuts import render, HttpResponse
from django.db.models import Prefetch
import pickle
from .models import Door, Color_outside, Color_inside, Size_door, Category_door


def index(request):
    doors = Door.objects.prefetch_related(Prefetch('sizes', queryset=Size_door.objects.all()),
                                          Prefetch('colors_inside', queryset=Color_inside.objects.all()),
                                          Prefetch('colors_outside', queryset=Color_outside.objects.all()))
    # for door in doors:
    #     for color in door.colors_inside.iterator():
    #         print(color.code)
    return render(request, 'main/index.html', context={'doors': doors})


def door_info(request, door_id):
    door = Door.objects.get(id=door_id)
    # for color in door.colors_inside.iterator():
    #     print(color.color, color.code)
    return render(request, 'main/shablon_door.html', context={'door': door})


def about(request):
    return render(request, 'main/about.html')


def assortment(request, category_id):
    doors = Door.objects.filter(category_id=category_id)
    category = Category_door.objects.get(id=category_id)
    return render(request, 'main/entrance_doors.html', context={'doors': doors, 'category': category})
