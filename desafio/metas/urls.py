from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMeta, name='lista-meta'),
    path('home/', views.home, name='home'),
    path('meta/<int:id>', views.metaView, name="meta-view"),
    path('novameta/', views.novaMeta, name="nova-meta"),
    path('edit/<int:id>', views.editMeta, name="edit-meta"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('delete/<int:id>', views.deleteMeta, name="delete-meta"),
    path('comentario/<int:id>', views.novoComentario, name="novo-comentario"),
    path('comentario/<int:id>/<int:porcentagem>', views.alterandoPorcentagem, name="alterando-porcentagem"),


]