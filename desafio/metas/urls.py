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
    path('changestatusS/<int:id>', views.changeStatusS, name="change-statusS"),
    path('changestatusC/<int:id>', views.changeStatusCor, name="change-status-cor"),
    path('changestatus/<int:id>/<int:porcentagem>', views.changeStatusSComentario, name="change-status-comentario"),
    path('changestatusS/<int:id>/<int:porcentagem>', views.changeStatusSSComentario, name="change-setor-status-comentario"),
    path('changestatusC/<int:id>/<int:porcentagem>', views.changeStatusCSComentario, name="change--status-comentario"),
    path('delete/<int:id>', views.deleteMeta, name="delete-meta"),
    path('deletadas/activate/<int:id>', views.activateMeta, name="activate-meta"),
    path('comentario/<int:id>', views.novoComentario, name="novo-comentario"),
    path('comentario/<int:id>/<int:porcentagem>', views.alterandoPorcentagem, name="alterando-porcentagem"),
    path('deletadas/', views.listaDeletadas, name="lista-deletadas"),
    path('<str:setorLista>', views.listaSetor, name="lista-setor"),
    path('metas/<str:cor>', views.listaCor, name="lista-cor"),
    path('sobre/', views.sobre, name="sobre"),
    path('deletamesmo/<int:id>', views.deletaMesmo, name="deleta-mesmo"),

]