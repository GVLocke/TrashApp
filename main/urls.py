from django.urls import path
from . import views

urlpatterns = [
  path("<String:name>", views.index, name="index"),
]
