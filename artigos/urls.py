from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_list, name='artigos_list'),
    path('<int:pk>/', views.artigo_detail, name='artigo_detail'),
    path('<int:pk>/like/', views.artigo_like, name='artigo_like'),
    path('criar/', views.artigo_create, name='artigo_create'),
    path('<int:pk>/editar/', views.artigo_update, name='artigo_update'),
    path('<int:pk>/apagar/', views.artigo_delete, name='artigo_delete'),
]
