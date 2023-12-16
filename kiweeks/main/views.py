from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.db.models import Prefetch
import pickle
from django.views.generic import ListView
from .models import Image, Item


# class DoorIndex(ListView):
#     model = Door
#     template_name = 'main/index.html'
#     context_object_name = 'doors'

def index(request):
    pass


def door_info(request, door_id):
    pass


def assortment(request, category):
    pass