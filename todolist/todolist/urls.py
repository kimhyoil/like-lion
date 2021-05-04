from django.contrib import admin
from django.urls import path, include
import todo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo.views.home, name="home"),
    path('create/', todo.views.create, name="create"),
    path('update/<str:id>', todo.views.update, name="update"),
    path('delete/<str:id>', todo.views.delete, name="delete")
]

