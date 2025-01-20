from django.urls import path
from .views import screenshare_view

urlpatterns = [
    path('', screenshare_view, name='screenshare'),
]
