from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('conocenos', views.quienessomos, name='conocenos'),
    path('arrendar', views.arrendar, name='arrendar'),
    path('registro', views.nuevousuario, name='nuevo'),
]