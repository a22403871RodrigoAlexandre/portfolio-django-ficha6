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
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('ucs/<int:uc_id>/', views.uc_detail_view, name='uc_detail'),
    path('projetos/<int:projeto_id>/', views.projeto_detail_view, name='projeto_detail'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('projetos/create/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:pk>/edit/', views.projeto_update, name='projeto_update'),
    path('projetos/<int:pk>/delete/', views.projeto_delete, name='projeto_delete'),
]