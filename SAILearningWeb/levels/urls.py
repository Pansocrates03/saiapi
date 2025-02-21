from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'levels'

urlpatterns = [
    path('', views.avance, name='avance'),
    path('nivel/<int:nivel>/', views.nivel, name='level'),
    path('nivel/<int:nivel>/', views.nivel_2, name='nivel2'),
]
