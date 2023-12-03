from django.urls import path, include
from . import views
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='main'),
    path('assortment/<category>', views.assortment, name='entrance'),
    path('door_info/<int:door_id>', views.door_info, name='door_info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

