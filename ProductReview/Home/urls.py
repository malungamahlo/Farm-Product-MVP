from django.urls import path
from .import views

#URLConf Module
urlpatterns = [
    path('' , views.home),
    path('form/', views.form),
]