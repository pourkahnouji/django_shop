from . import views
from django.urls import path

app_name = 'templates'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]
