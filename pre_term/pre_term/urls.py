"""pre_term URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.views.static import serve

from pre_term import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('App.urls', namespace='app')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('diamond', TemplateView.as_view(template_name="index.html")),
    path('diamond/inbox', TemplateView.as_view(template_name="index.html")),
    path('diamond/inbox/collaboratorRemind', TemplateView.as_view(template_name="index.html")),
    path('diamond/inbox/invite', TemplateView.as_view(template_name="index.html")),
    path('diamond/inbox/documentRemind', TemplateView.as_view(template_name="index.html")),
    path('diamond/inbox/kickOutRemind', TemplateView.as_view(template_name='index.html')),
    path('diamond/dashboard/team/<teamId>', TemplateView.as_view(template_name="index.html")),
    path('diamond/searchDocument/', TemplateView.as_view(template_name="index.html")),
    path('diamond/templates/<teamId>', TemplateView.as_view(template_name="index.html")),
    path('diamond/createTeam', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/used', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/desktop', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/favorites', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/own', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/team', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard/trash', TemplateView.as_view(template_name="index.html")),
    path('diamond/dashboard', TemplateView.as_view(template_name="index.html")),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('editor/<documentId>', TemplateView.as_view(template_name='index.html')),
    path('error/', TemplateView.as_view(template_name='index.html')),
    path('diamond/profile/', TemplateView.as_view(template_name='index.html')),
    path('diamond/profile/changeusername', TemplateView.as_view(template_name='index.html')),
    path('diamond/profile/changepassword', TemplateView.as_view(template_name='index.html')),
    path('diamond/profile/changeicon', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),
    path('diamond/searchteam/', TemplateView.as_view(template_name='index.html')),
    path('changefile/<fileId>', TemplateView.as_view(template_name='index.html')),
    path('templatepreview/<templateid>', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
