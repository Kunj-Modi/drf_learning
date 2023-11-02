from django.urls import path

from . import views

urlpatterns = [
    path('emp/<int:pk>', views.emp_retrieve, name='emp_retrieve'),
    path('dep/<int:pk>', views.dep_retrieve, name='dep_retrieve'),
]
