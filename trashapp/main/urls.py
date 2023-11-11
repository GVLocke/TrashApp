from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/receive-distance/', views.receive_distance_data, name='receive_distance_data'),
    path('create-trash-can/', views.create_trash_can, name='create_trash_can')
]
