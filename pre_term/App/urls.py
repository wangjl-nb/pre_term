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
    # path('add_team/',views.add_team,name='add_team'),
    path('teams_show/',views.teams_show, name='teams_show'),
    path('team_info/', views.team_info, name='team_info'),
    path('create_file/',views.create_file,name='create_file'),
    path('change_file/',views.change_file,name='change_file'),
]
