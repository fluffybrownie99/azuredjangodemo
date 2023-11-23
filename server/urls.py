"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views #import from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', views.notes_handler, name='notes_handler'),
    path('note/<str:note_id>/', views.get_note_by_id, name='get_note_by_id'),
    path('note/update/<str:note_id>/', views.update_note, name='update_note'),
    path('note/delete/<str:note_id>/', views.delete_note, name='delete_note'),
    ]

