from django.urls import path
from .views import asosiy

urlpatterns = [
    path('', asosiy, name='asosiy'),
]
