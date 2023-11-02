from django.urls import path

from . import views

urlpatterns = [
    path('create_emp/', views.emp_create, name='emp_create'),
    path('create_dep/', views.dep_create, name='dep_create'),
]
