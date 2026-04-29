from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tfcs/<int:tfc_id>/', views.tfc_detail_view, name='tfc_detail'),

    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('ucs/<int:uc_id>/', views.uc_detail_view, name='uc_detail'),
    path('projetos/<int:projeto_id>/', views.projeto_detail_view, name='projeto_detail'),
    path('makingof/', views.makingof_view, name='makingof'),

    path('projetos/create/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:pk>/edit/', views.projeto_update, name='projeto_update'),
    path('projetos/<int:pk>/delete/', views.projeto_delete, name='projeto_delete'),

    path('licenciaturas/<int:lic_id>/', views.licenciatura_detail_view, name='licenciatura_detail'),
    path('licenciaturas/create/', views.licenciatura_create, name='licenciatura_create'),
    path('licenciaturas/<int:pk>/edit/', views.licenciatura_update, name='licenciatura_update'),
    path('licenciaturas/<int:pk>/delete/', views.licenciatura_delete, name='licenciatura_delete'),
    
    path('tecnologias/create/', views.tecnologia_create, name='tecnologia_create'),
    path('tecnologias/<int:pk>/edit/', views.tecnologia_update, name='tecnologia_update'),
    path('tecnologias/<int:pk>/delete/', views.tecnologia_delete, name='tecnologia_delete'),

    path('competencias/create/', views.competencia_create, name='competencia_create'),
    path('competencias/<int:pk>/edit/', views.competencia_update, name='competencia_update'),
    path('competencias/<int:pk>/delete/', views.competencia_delete, name='competencia_delete'),

    path('formacoes/create/', views.formacao_create, name='formacao_create'),
    path('formacoes/<int:pk>/edit/', views.formacao_update, name='formacao_update'),
    path('formacoes/<int:pk>/delete/', views.formacao_delete, name='formacao_delete'),
    path('docentes/<int:docente_id>/', views.docente_detail_view, name='docente_detail'),

    path('sobre/', views.sobre_view, name='sobre'),
]