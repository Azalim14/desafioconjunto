from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMeta, name='lista-meta'),
    path('meta/<int:id>', views.metaView, name="meta-view"),
]