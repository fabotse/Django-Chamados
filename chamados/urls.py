from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chamado/<str:pk>/', views.chamado, name='chamado'),
    path('create_chamado/', views.create_chamado, name='create_chamado'),
    path('update_chamado/<str:pk>/', views.update_chamado, name='update_chamado'),
    path('delete_chamado/<str:pk>/', views.delete_chamado, name='delete_chamado'),

]
