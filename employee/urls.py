from django.urls import path

from . import views

urlpatterns = [
    path('create_emp/', views.emp_create, name='emp_create'),
    path('list_emp/', views.list_emp, name='list_emp'),
    path('create_dep/', views.dep_create, name='dep_create'),
]
