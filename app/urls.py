from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hey, name="hey"),
    path('getUsers/', views.GetUsers.as_view(), name="get_users"),
    path('student/', include('student.urls'), name='student'),
    path('employee/', include('employee.urls'), name='employee'),
]
