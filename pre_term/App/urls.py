from django.urls import path, re_path
from App import views

app_name='app'

urlpatterns=[
    path('index',views.index,name='index'),
]