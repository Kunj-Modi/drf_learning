from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hey, name="hey"),
    path('student/', include('student.urls'), name='student')
]
