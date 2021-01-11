from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMeta, name='lista-meta'),
    path('meta/<int:id>', views.metaView, name="meta-view"),
    path('novameta/', views.novaMeta, name="nova-meta"),
    path('edit/<int:id>', views.editMeta, name="edit-meta"),
    path('delete/<int:id>', views.deleteMeta, name="delete-meta"),

]