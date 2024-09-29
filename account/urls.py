from . import views
from django.urls import path

app_name = 'templates'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('search/', views.search, name='search'),

]
