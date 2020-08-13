import json
import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.urls import reverse
from App.models import *
from App.views_helper import send_email_activate


def add_team(request):
    for i in range(1, 30):
        team = Team()
        team.name = '团队' + str(i)
        team.describe = '这是第' + str(i) + '个团队'
        team.icon = 'suoluetubig.jpg'
        team.save()
        team_relation = Team_relation()
        team_relation.user_id = 2
        team_relation.team = team
        team_relation.save()
    return JsonResponse(data={'code': 'ok'})


# 加入团队
def teams_show(request):
    user = request.user
    teams = Team.objects.filter(team_relation__user=user).order_by('-id')
    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(teams, perpage)

    page_object = paginator.page(page)
    data = {'msg': '团队信息', 'teams': page_object, "page_range": paginator.page_range}
    return render(request, 'team/team_search.html', context=data)


# 团队信息展示
def team_info(request):
    team_id = request.GET.get('team_id', 4)
    team = Team.objects.get(pk=team_id)
    # relation = Team_relation.objects.
    team_relations = Team_relation.objects.filter(team_id=team_id)
    level = team_relations.filter(user=request.user).first().level
    return render(request, 'team/teaminfo.html',
                  context={'team': team, 'team_relations': team_relations, 'level': level})


def dissmiss_team(request):
    team_id = request.GET['team_id']
    team = Team.objects.get(pk=team_id)
    team.delete()
    return HttpResponse('解散成功')


def create_team(request):
    if request.method == 'GET':

        data = {
            "title": "创建团队",
        }

        return render(request, 'team/create_team.html', context=data)

    elif request.method == 'POST':

        name = request.POST.get("teamname")
        tteam = Team.objects.filter(name=name)
        if tteam.exists():
            return HttpResponse('团队名已存在')
        else:
            describe = request.POST.get("describe")
            icon = request.FILES.get("icon")
            if icon == None:
                icon = "suoluetubig.jpg"
            team = Team()
            team.name = name
            team.describe = describe
            team.icon = icon
            team.save()
            team_relation = Team_relation()
            team_relation.user = request.user
            team_relation.team = team
            team_relation.level = 2
            team_relation.change = True
            team_relation.comment = True
            team_relation.save()
            team_relations = Team_relation.objects.filter(team_id=team.id)
            level = team_relations.filter(user=request.user).first().level
            return render(request, 'team/teaminfo.html',
                          context={'team': team, 'team_relations': team_relations, 'level': level})


def team_search(request):
    if request.method == 'GET':
        return render(request, 'team/team_search.html')
    elif request.method == 'POST':
        content = request.POST.get('search_content')
        teams = Team.objects.filter(Q(name__icontains=content) | Q(describe__icontains=content))
        return render(request, 'team/team_search.html', context={'teams': teams})


def team_application(request):
    team_id = request.GET['team_id']
    user_id = request.user.id
    relation = Team_relation.objects.filter(user_id=user_id).filter(team_id=team_id)
    if relation.exists():
        return HttpResponse('您已加入团队')
    apply = Team_application.objects.filter(user_id=user_id).filter(team_id=team_id)
    if apply.exists():
        return HttpResponse('对不起，你已申请该团队，请耐心等待')
    else:
        apply = Team_application()
        apply.team_id = team_id
        apply.user_id = user_id
        apply.save()
    return HttpResponse('申请成功！')


def deal_application(request):
    team_id = request.GET.get('team_id')
    applications = Team_application.objects.filter(team_id=team_id)
    return render(request, 'team/deal_application.html', context={'applications': applications})


def process_application(request):
    apply_id = request.GET.get('applyid')
    application = Team_application.objects.get(pk=apply_id)
    if request.GET.get('type') == 'agree':
        team = Team.objects.get(pk=application.team_id)
        team.number_num = team.number_num + 1
        team.save()
        team_relation = Team_relation()
        team_relation.level = 1
        team_relation.team = team
        team_relation.user = application.user
        team_relation.save()
        data = {
            "msg": "add success",
        }
    else:
        data = {
            "msg": "refuse success",
        }
    application.delete()
    return JsonResponse(data=data)


def deal_change(request):
    relation_id = request.GET.get('relation_id')
    team_relation = Team_relation.objects.get(pk=relation_id)
    team_relation.change = not team_relation.change
    team_relation.save()
    return JsonResponse(data={"msg": "修改文档修改权限成功"})


def deal_comment(request):
    relation_id = request.GET.get('relation_id')
    team_relation = Team_relation.objects.get(pk=relation_id)
    team_relation.comment = not team_relation.comment
    team_relation.save()
    return JsonResponse(data={"msg": "修改文档评论权限成功"})


def invite_teamworker(request):
    team_id = request.GET['team_id']
    team = Team.objects.get(pk=team_id)
    user = User.objects.get(pk=request.GET['user'])

    team_relation = Team_relation.objects.filter(user=user).filter(team=team)
    if team_relation.exists():
        return HttpResponse("该用户已加入团队")

    team.number_num = team.number_num + 1
    team_relation = Team_relation()
    team_relation.level = 1
    team_relation.team = team
    team_relation.user = user
    team_relation.save()

    return render(request, 'team/teaminfo.html', context={"team": team})


# 修改团队信息
def team_info_change(request):
    teamname = request.POST.get("teamname")
    icon = request.FILES.get("icon")

    team = Team.objects.get(pk=request.GET['team_id'])

    team.name = teamname
    if icon != None:
        team.icon = icon
    team.save()
    return HttpResponse('团队信息修改成功')


# 团队文件列表
def team_files_list(request):
    level = request.GET['level']
    team = Team.objects.get(pk=request.GET['team_id'])
    files = File.objects.filter(team_record__team=team).filter(is_delete=False).order_by('-id')
    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(files, perpage)
    team_id = request.GET['team_id']

    page_object = paginator.page(page)
    data = {'msg': '团队文档列表', 'files': page_object, "page_range": paginator.page_range, "team_id": team_id,
            "level": level}
    return render(request, 'file/team_files_list.html', context=data)


# 团队文档分享权限
def deal_share(request):
    team = Team.objects.get(pk=request.GET['team_id'])
    file = File.objects.get(pk=request.GET['file_id'])
    team_record = Team_record.objects.filter(team=team).filter(file=file)
    team_record.is_share = not team_record.is_share
    team_record.save()
    return JsonResponse(data={"msg": "修改文档分享权限成功"})


# 发送邀请加入团队
def team_invitation(request):
    team_id = request.GET['team_id']
    user_id = request.GET['user_id']
    relation = Team_relation.objects.filter(user_id=user_id).filter(team_id=team_id)
    if relation.exists():
        return HttpResponse('该用户已加入团队')
    invite = Team_application.objects.filter(user_id=user_id).filter(team_id=team_id)
    if invite.exists():
        return HttpResponse('对不起，你已邀请该用户，请耐心等待')
    else:
        invite = Team_invitation()
        invite.user_id = user_id
        invite.team_id = team_id
        invite.save()
    return HttpResponse('邀请成功！')


# 踢出成员
def kick(request):
    team_relation = Team_relation.objects.get(pk=request.GET['relation_id'])
    team = team_relation.team
    team.number_num = team.number_num - 1
    team.save()
    team_relation.delete()
    return HttpResponse('踢出人员成功')


# 处理邀请
def process_invitation(request):
    invite_id = request.GET.get('inviteid')
    invitation = Team_invitation.objects.get(pk=invite_id)
    if request.GET.get('type') == 'agree':
        team = Team.objects.get(pk=invitation.team_id)
        team.number_num = team.number_num + 1
        team.save()
        team_relation = Team_relation()
        team_relation.level = 1
        team_relation.team = team
        team_relation.user = invitation.user
        team_relation.save()
        data = {
            "msg": "add success",
        }
    else:
        data = {
            "msg": "refuse success",
        }
    invitation.delete()
    return JsonResponse(data=data)


def exit_team(request):
    team_id = request.GET['team_id']
    team = Team.objects.get(pk=team_id)
    team_relation = Team_relation.objects.filter(team_id=team_id).filter(user=request.user)
    team_relation.delete()
    team.number_num = team.number_num - 1
    team.save()
    return HttpResponse('退出团队成功')
