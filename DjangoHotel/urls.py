from django.urls import path

from django.contrib import admin
from .views import HotelListView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('admin/', admin.site.urls),
]
