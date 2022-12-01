from django.urls import path, include

from . import views

urlpatterns = [
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher_create/', views.create_teacher, name='teacher_create'),

]
