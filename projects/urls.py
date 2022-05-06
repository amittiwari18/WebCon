

from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-Project/', views.createProject, name="create-Project"),
    path('update-Project/<str:pk>', views.updateProject, name="update-Project"),
    path('delete-Project/<str:pk>', views.deleteProject, name="delete-Project"),

]