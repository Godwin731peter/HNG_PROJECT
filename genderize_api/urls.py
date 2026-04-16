from django.urls import path, include
from . import views

urlpatterns = [
    path('classify/', views.task0, name='classify-task'),
    path('health/', views.health),
]