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
    path('destroy_file/',views.destroy_file,name='destroy_file'),
    path('create_team_file/',views.create_team_file,name='create_team_file'),
    path('dissmiss_team/',views.dissmiss_team,name='dismiss_team'),
    path('create_team/', views.create_team, name='create_team'),
    path('user_info_change/', views.user_info_change, name='user_info_change'),
    path('team_search/',views.team_search,name='team_search'),
    path('team_application/',views.team_application,name='team_application'),
    path('deal_application/',views.deal_application,name='deal_application'),
    path('process_application/',views.process_application,name='process_application'),
    path('deal_change/',views.deal_change,name='deal_change'),
    path('deal_comment/',views.deal_comment,name='deal_comment'),
    path('user_search/', views.user_search, name='user_search'),
    path('invite_teamworker/', views.invite_teamworker, name='invite_teamworker'),
]
