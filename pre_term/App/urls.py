from django.urls import path, re_path
from App import views

app_name = 'app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("is_login/",views.is_login,name='is_login'),
    path('activate/', views.activate, name='activate'),
    path('user_info/', views.user_info, name='user_info'),
    path('logout/', views.logout, name='logout'),
    path('team_info/', views.team_info, name='team_info'),
    path('change_file/)', views.change_file, name='change_file'),
    path('my_files_list/', views.my_files_list, name='my_files_list'),
    path('file_info/', views.file_info, name='file_info'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('file_log/',views.file_log,name='file_log'),
    path('personal_delete_files/', views.personal_delete_files, name='personal_delete_files'),
    path('recover_file/', views.recover_file, name='recover_file'),
    path('destroy_file/',views.destroy_file,name='destroy_file'),
    path('create_team_file/',views.create_team_file,name='create_team_file'),
    path('dissmiss_team/',views.dismiss_team,name='dismiss_team'),
    path('create_team/', views.create_team, name='create_team'),
    path('change_password/', views.change_password, name='user_info_change'),
    path('team_search/',views.team_search,name='team_search'),
    path('deal_change/',views.deal_change,name='deal_change'),
    path('deal_comment/',views.deal_comment,name='deal_comment'),
    path('search_person/', views.search_person, name='user_search'),
    path('team_info_change/', views.team_info_change, name='team_info_change'),
    path('file_search/', views.file_search, name='file_search'),
    path('team_files_list/', views.team_files_list, name='team_files_list'),
    path('deal_share/',views.deal_share,name='deal_share'),
    path('exit_team/',views.exit_team,name='exit_team'),
    path('kick/',views.kick,name='kick'),
    path('deal_collect/', views.deal_collect, name='deal_collect'),
    path('change_name/',views.change_name,name='change_name'),
    path('change_icon/',views.change_icon,name='change_icon'),
    path('my_teams/', views.my_teams, name='my_teams'),
    path('change_teamname/',views.change_teamname,name='change_teamname'),
    path('change_team_describe/', views.change_team_describe, name='change_team_describe'),
    path('get_templetes/', views.get_templetes, name='get_templetes'),
    path('grade_templetes/', views.grade_templetes, name='grade_templetes'),
    path('create_file/', views.create_file, name='create_file'),
    path('grant_power/', views.grant_power, name='grant_power'),
    # path('deal_application/',views.deal_application,name='deal_application'),
    path('team_invitation/', views.team_invitation, name='team_invitation'),
    path('invitation_list/', views.invitation_list, name='invitation_list'),
    path('process_invitation/',views.process_invitation,name='process_invitation'),
    path('team_application/',views.team_application,name='team_application'),
    path('process_application/',views.process_application,name='process_application'),
    path('application_list/', views.application_list, name='application_list'),
    path('change_team_icon/', views.change_team_icon, name='change_team_icon'),
    path('grant_team_power/', views.grant_team_power, name='grant_team_power'),
    path('set_is_share/', views.set_is_share, name='set_is_share'),
    path('cooperate_invitation/', views.cooperate_invitation, name='cooperate_invitation'),
    path('coinvitation_list/', views.coinvitation_list, name='coinvitation_list'),
    path('process_coinvitation/', views.process_coinvitation, name='process_coinvitation'),
    path('change_file/',views.change_file, name='change_file'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('file_content/',views.file_content,name='file_content'),
    path('message_list/', views.message_list, name='message_list'),
    path('delete_message/',views.delete_message,name='delete_message'),
    path('comment_reminder/',views.comment_reminder,name='comment_reminder'),
    path('delete_comment_reminder/',views.delete_comment_reminder,name='delete_comment_reminder'),
    path('template_content/',views.template_content,name='template_content'),
    path('get_change_power/',views.get_change_power,name='get_change_power'),
    path('abandon_change_power/',views.abandon_change_power,name='abandon_change_power'),
]
