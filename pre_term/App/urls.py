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
    path('teams_show/', views.teams_show, name='teams_show'),
    path('team_info/', views.team_info, name='team_info'),
    path('create_file/', views.create_file, name='create_file'),
    re_path('change_file/(?P<file_id>\d+)', views.change_file, name='change_file'),
    path('my_files_list/', views.my_files_list, name='my_files_list'),
    re_path('file_info/(?P<file_id>\d+)', views.file_info, name='file_info'),
    re_path('delete_file/(?P<file_id>\d+)', views.delete_file, name='delete_file'),
    path('file_log/',views.file_log,name='file_log'),
    path('delete_files_list/', views.delete_files_list, name='delete_files_list'),
    re_path('recover_file/(?P<file_id>\d+)', views.recover_file, name='recover_file'),
]
