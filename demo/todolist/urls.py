from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_list,name='task_list'),
    path('task/<int:task_id>/',views.task_detail,name='task_detail'),
    path('task/<int:task_id>/update/',views.update_task_status,name='update_task_status'),
]