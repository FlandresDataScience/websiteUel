from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('program/<str:program_title>', views.program, name='program'),
    path('historia', views.historia, name='historia'),
    path('corpos', views.corpos, name='corpos'),
    path('orgaos', views.orgaos, name='orgaos'),
    path('canais', views.canais, name='canais'),
    path('arte', views.arte, name='arte'),
    path('esportes', views.esportes, name='esportes'),
    path('vida', views.vida, name='vida'),
    path('graduacao', views.graduacao, name='graduacao'),
    path('post', views.post, name='post'),
    path('mestrado', views.mestrado, name='mestrado'),
    path('doutorado', views.doutorado, name='doutorado'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('laboratorios', views.laboratorios, name='laboratorios'),
    path('extensao', views.extensao, name='extensao'),
    path('assessoria', views.assessoria, name='assessoria'),
    path('guia_estudante', views.guia_estudante, name='guia_estudante'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
]
