from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.db.models import Prefetch
import pickle
from django.views.generic import ListView
from .models import Door, Color_outside, Color_inside, Size_door, Category_door


# class DoorIndex(ListView):
#     model = Door
#     template_name = 'main/index.html'
#     context_object_name = 'doors'

def index(request):
    doors = Door.objects.prefetch_related(Prefetch('sizes', queryset=Size_door.objects.all()),
                                          Prefetch('colors_inside', queryset=Color_inside.objects.all()),
                                          Prefetch('colors_outside', queryset=Color_outside.objects.all()))
    paginator = Paginator(doors, 48)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # for door in doors:
        # print(len(door.photo_door_set.all()))
        # for photo in door.photo_door_set.all:
        #     print(photo)
    return render(request, 'main/index.html', context={'page_obj':page_obj, 'doors': doors})


def door_info(request, door_id):
    door = Door.objects.get(id=door_id)
    # for color in door.colors_inside.iterator():
    #     print(color.color, color.code)
    return render(request, 'main/shablon_door.html', context={'door': door})


def assortment(request, category):
    category = Category_door.objects.get(link_text=category)
    doors = Door.objects.filter(category_id=category.id)

    paginator = Paginator(doors, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/entrance_doors.html', context={'page_obj': page_obj, 'doors': doors, 'category': category})