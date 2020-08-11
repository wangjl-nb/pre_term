from django.urls import path, re_path
from App import views

app_name = 'app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('activate/', views.activate, name='activate'),
    path('user_info/', views.user_info, name='user_info'),
    path('logout/', views.logout, name='logout'),
]
