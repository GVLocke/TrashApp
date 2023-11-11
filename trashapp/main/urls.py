from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/receive-distance/', views.receive_distance_data, name='receive_distance_data'),
    path('delete_trash_can/<int:trash_can_id>/', views.delete_trash_can, name='delete_trash_can'),
    path('api/get-latest-distance/<str:trash_can_name>/', views.get_lastest_distance, name='get_lastest_distance'),
    path('create-trash-can/', views.create_trash_can, name='create_trash_can')
]
