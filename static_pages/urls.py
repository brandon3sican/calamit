from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('project-1',views.project1,name="project-1"),
    path('project-2',views.project2,name="project-2"),
]