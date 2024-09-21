from . import views
from django.urls import path

app_name = 'templates'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.log_out, name='logout'),
<<<<<<< HEAD
    path('search/', views.search, name='search'),
=======
>>>>>>> 45fa0c1a8018d24633e1628bb02082078aaa02c4
]
