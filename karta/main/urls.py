from django.urls import path
from .views import asosiy

url_paterns=[
    path('',asosiy,name=asosiy)
]
