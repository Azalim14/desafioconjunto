from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMeta, name='lista-meta'),
    
]