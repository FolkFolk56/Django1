from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('Folk/', views.Folk, name='Folk'),
]
