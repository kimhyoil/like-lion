from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.read, name="home"),
    path('newpost/', views.create, name="newpost"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
