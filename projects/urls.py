from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('github/', views.github_projects, name='github_projects'),
]
