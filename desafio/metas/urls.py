from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaMeta, name='lista-meta'),
    path('home/', views.home, name='home'),
    path('meta/<int:id>', views.metaView, name="meta-view"),
    path('novameta/', views.novaMeta, name="nova-meta"),
    path('novameta/<str:setorP>', views.novaMetaSetor, name="nova-meta-setor"),
    path('edit/<int:id>', views.editMeta, name="edit-meta"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('delete/<int:id>', views.deleteMeta, name="delete-meta"),
    path('deletadas/activate/<int:id>', views.activateMeta, name="activate-meta"),
    path('comentario/<int:id>', views.novoComentario, name="novo-comentario"),
    path('comentario/<int:id>/<int:porcentagem>', views.alterandoPorcentagem, name="alterando-porcentagem"),
    path('deletadas/', views.listaDeletadas, name="lista-deletadas"),
    path('<str:setorLista>', views.listaSetor, name="lista-setor"),
    path('sobre/', views.sobre, name="sobre"),
    path('deletamesmo/<int:id>', views.deletaMesmo, name="deleta-mesmo"),

]