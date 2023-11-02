from django.urls import path

from . import views

urlpatterns = [
    path('random/', views.random, name="random"),
    path('all/', views.get_all, name="get_all"),
    path('add/', views.add_student, name='add'),
]
