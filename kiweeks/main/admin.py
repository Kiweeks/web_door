from django.contrib import admin
from .models import Door, Color_inside, Color_outside, Photo_door, Type_door, Size_door, Category_door, Side_of_door, Photo_accessories

admin.site.register(Door)
admin.site.register(Color_outside)
admin.site.register(Color_inside)
admin.site.register(Photo_door)
admin.site.register(Type_door)
admin.site.register(Size_door)
admin.site.register(Category_door)
admin.site.register(Side_of_door)
admin.site.register(Photo_accessories)