import datetime
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


# 团队信息展示
def team_info(request):
    try:
        team_id = int(request.GET['team_id'])
        team = Team.objects.get(pk=team_id)
        user = request.user
        team_relations = Team_relation.objects.filter(team=team)
        list = []
        for team_relation in team_relations:
            if team_relation.level == 2:
                user2 = team_relation.user
            elif team_relation.level == 1:
                dic2 = {
                    "id": team_relation.user.id,
                    "u_icon": str(team_relation.user.u_icon),
                    "u_username": team_relation.user.u_username,
                    "change": team_relation.change,
                    "comment": team_relation.comment
                }
                list.append(dic2)
        dic = {

        }

        if Team_relation.objects.filter(Q(team=team) & Q(user=user)).first().level == 2:
            type = 0
        elif Team_relation.objects.filter(Q(team=team) & Q(user=user)).first().level == 1:
            type = 1
        else:
            type = 2
        data = {'msg': '团队信息介绍',
                'name': team.name,
                'icon': str(team.icon),
                'describe': team.describe,
                'create_date': team.create_date,
                'number_num': team.number_num,
                'u_id': user2.id,
                'u_icon': str(user2.u_icon),
                'u_username': user2.u_username,
                'type': type,
                'list': list}
    except:
        data = {
            'msg': '获取团队介绍失败，团队id不存在'
        }
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


def dismiss_team(request):
    try:
        team_id = request.POST['id']
        team = Team.objects.get(pk=team_id)
        team.delete()
        return JsonResponse(data={"msg": "解散成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "解散失败", "status": 1})


def team_search(request):
    content = request.POST.get('key')
    teams = Team.objects.filter(Q(name__icontains=content) | Q(describe__icontains=content))
    list = []
    for team in teams:
        dic = {
            "id": team.id,
            "name": team.name,
            "description": team.describe,
            "number": team.number_num,
        }
        list.append(dic)
    data = {
        "msg": "团队列表",
        "list": list,
    }
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


def deal_application(request):
    team_id = request.GET.get('team_id')
    applications = Team_application.objects.filter(team_id=team_id)
    return render(request, 'team/deal_application.html', context={'applications': applications})


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
    team_id = int(request.GET['team_id'])
    team = Team.objects.get(pk=team_id)
    files = File.objects.filter(team_record__team=team).filter(is_delete=False).order_by('-id')

    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(files, perpage)

    page_object = paginator.page(page)
    res = []
    for file in page_object:
        dic = {
            "id": file.id,
            "title": file.title,
            "create_date": file.create_date,
            "creator": file.creator,
        }
        log = File_log.objects.filter(file=file).order_by("-change_date").first()
        if log:
            dic["change_date"] = log.change_date
            dic["u_username"] = log.user.u_username
        res.append(dic)
    data = {'msg': '团队文档列表', "documentList": res}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


# 时间格式化
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


# 团队文档分享权限
def deal_share(request):
    team = Team.objects.get(pk=request.GET['team_id'])
    file = File.objects.get(pk=request.GET['file_id'])
    team_record = Team_record.objects.filter(team=team).filter(file=file)
    team_record.is_share = not team_record.is_share
    team_record.save()
    return JsonResponse(data={"msg": "修改文档分享权限成功"})


# 踢出成员
def kick(request):
    try:
        team_id = request.POST['id']
        user_id = request.POST['u_id']
        user_level = Team_relation.objects.filter(user=request.user).filter(team_id=team_id).first().level
        print(user_level)
        if user_level < 2:
            return JsonResponse(data={"msg": "踢人权限不够", "status": 1})
        team_relation = Team_relation.objects.filter(user_id=user_id).filter(team_id=team_id).first()
        team = team_relation.team
        team.number_num = team.number_num - 1
        team.save()
        team_relation.delete()
        message = Message()
        message.user_id = user_id
        message.content = '您已被踢出团队' + team.name
        message.save()
        return JsonResponse(data={"msg": "踢出成员成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "踢出成员失败", "status": 1})


def exit_team(request):
    try:
        team_id = request.POST['id']
        team = Team.objects.get(pk=team_id)
        team_relation = Team_relation.objects.filter(team_id=team_id).filter(user=request.user)
        team_relation.delete()
        team.number_num = team.number_num - 1
        team.save()
        return JsonResponse(data={"msg": "退出成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "退出失败", "status": 1})


# 我所参加的团队
def my_teams(request):
    user = request.user
    teams = Team.objects.filter(team_relation__user=user)
    if teams.exists:
        res = []
        for team in teams:
            level = Team_relation.objects.filter(team=team).filter(user=user).first().level
            dic = {
                "id": team.id,
                "name": team.name,
                "description": str(team.describe),
                "level": str(level),
            }
            res.append(dic)
        data = {
            'msg': '我加入的团队',
            'teams': res,
        }
    else:
        data = {
            'msg': '没有加入任何团队'
        }
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


def change_teamname(request):
    team = Team.objects.get(pk=request.POST['team_id'])
    name = request.POST.get('team_name')
    exist_team = Team.objects.filter(name=name)
    if not exist_team.exists():
        team.name = name
        team.save()
        data = {
            "msg": "修改成功",
            "status": 0,
        }
    else:
        data = {
            "msg": "修改失败",
            "status": 1,
        }
    return JsonResponse(data=data)


def change_team_describe(request):
    try:
        team = Team.objects.get(pk=request.POST['team_id'])
        describe = request.POST.get('describe')
        team.describe = describe
        team.save()
        data = {
            "msg": "修改成功",
            "status": 0,
        }
    except:
        data = {
            "msg": "修改失败",
            "status": 1,
        }
    return JsonResponse(data=data)


# 发送邀请加入团队
def team_invitation(request):
    try:
        team_id = int(request.POST['team_id'])
        user_id = int(request.POST['user_id'])
        reason = request.POST['reason']
        team = Team.objects.get(pk=team_id)
        relation = Team_relation.objects.filter(user_id=user_id).filter(team_id=team_id)
        if relation.exists():
            data = {
                'msg': '该用户已加入团队',
                'status': 1
            }
            return JsonResponse(data=data)
        invite = Team_invitation.objects.filter(user_id=user_id).filter(team_id=team_id)
        if invite.exists():
            data = {
                'msg': '对不起，你已邀请该用户，请耐心等待',
                'status': 1
            }
            return JsonResponse(data=data)
        invite = Team_invitation()
        invite.user_id = user_id
        invite.team_id = team_id
        invite.reason = reason
        invite.save()
        data = {
            'msg': '邀请成功！',
            'status': 0
        }
    except:
        data = {
            'msg': 'wrong',
            'status': 1
        }
    return JsonResponse(data=data)


# 查看邀请
def invitation_list(request):
    try:
        team_invitations = Team_invitation.objects.filter(user=request.user)
        res = []
        for team_invitation in team_invitations:
            team = Team.objects.get(pk=team_invitation.team_id)
            user = User.objects.filter(team_relation__team=team).filter(team_relation__level=2).first()
            dic = {
                "invitation_id": team_invitation.id,
                "u_username": user.u_username,
                "name": team.name,
                "reason": team_invitation.reason
            }
            res.append(dic)
        data = {
            'msg': '查看成功',
            'list': res
        }
    except:
        data = {
            'msg': '查看失败'
        }
    return JsonResponse(data=data)


# 处理邀请
def process_invitation(request):
    try:
        invitation_id = request.POST.get('id')
        invitation = Team_invitation.objects.get(pk=invitation_id)
        type = int(request.POST['type'])
        if type == 0:
            team = Team.objects.get(pk=invitation.team_id)
            team.number_num = team.number_num + 1
            team.save()
            team_relation = Team_relation()
            team_relation.level = 1
            team_relation.team = team
            team_relation.user = invitation.user
            team_relation.save()
            invitation.delete()
            data = {
                "msg": "已接受邀请",
                'status': 0
            }
        elif type == 1:
            data = {
                "msg": "已拒绝邀请",
                'status': 0
            }
            invitation.delete()
        else:
            data = {
                'msg': '请输入0或1',
                'status': 1
            }
    except:
        data = {
            'msg': 'wrong',
            'status': 1
        }
    return JsonResponse(data=data)


# 发送申请
def team_application(request):
    try:
        team_id = request.POST['id']
        user_id = request.user.id
        reason = request.POST['reason']
        relation = Team_relation.objects.filter(user_id=user_id).filter(team_id=team_id)
        if relation.exists():
            return JsonResponse(data={"msg": "您已是成员", "status": 1})
        apply = Team_application.objects.filter(user_id=user_id).filter(team_id=team_id)
        if apply.exists():
            return JsonResponse(data={"msg": "您已发送申请", "status": 1})
        else:
            apply = Team_application()
            apply.team_id = team_id
            apply.user_id = user_id
            apply.reason = reason
            apply.save()
        return JsonResponse(data={"msg": "申请成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "发生了未知错误", "status": 1})


# 查看申请
def application_list(request):
    try:
        team_id = int(request.GET['team_id'])
        team_applications = Team_application.objects.filter(team_id=team_id)
        res = []
        for team_application in team_applications:
            user = User.objects.get(pk=team_application.user_id)
            dic = {
                "application_id": team_application.id,
                "u_username": user.u_username,
                "reason": team_application.reason
            }
            res.append(dic)
        data = {
            'msg': '查看成功',
            'status': 0,
            'list': res
        }
    except:
        data = {
            'msg': '查看失败',
            'status': 1
        }
    return JsonResponse(data=data)


# 处理申请
def process_application(request):
    try:
        application_id = request.POST.get('id')
        print(application_id)
        application = Team_application.objects.get(pk=application_id)
        print(application)
        type = int(request.POST['type'])
        if type == 0:
            team = Team.objects.get(pk=application.team_id)
            team.number_num = team.number_num + 1
            team.save()
            team_relation = Team_relation()
            team_relation.level = 1
            team_relation.team = team
            team_relation.user = application.user
            team_relation.save()
            application.delete()
            data = {
                "msg": "已同意申请",
                'status': 0
            }
        elif type == 1:
            data = {
                "msg": "已拒绝申请",
                'status': 0
            }
            application.delete()
        else:
            data = {
                'msg': '请输入0或1',
                'status': 1
            }
    except:
        data = {
            'msg': 'wrong',
            'status': 1
        }
    return JsonResponse(data=data)


# 修改团队头像
def change_team_icon(request):
    try:
        icon = request.FILES.get('icon')
        team_id = int(request.POST['team_id'])
        team = Team.objects.get(pk=team_id)
        team.icon = icon
        team.save()

        data = {
            'msg': '修改成功',
            'status': 0
        }
    except:
        data = {
            'msg': '修改失败',
            'status': 1
        }
    return JsonResponse(data=data)


def grant_team_power(request):
    try:
        u_id = int(request.GET['u_id'])
        team_id = int(request.GET['team_id'])
        comment = int(request.GET['comment'])
        change = int(request.GET['change'])
        team_relation = Team_relation.objects.filter(team_id=team_id).filter(user_id=u_id).first()
        if comment == 0:
            team_relation.comment = True
            team_relation.save()
        elif comment == 1:
            team_relation.comment = False
            team_relation.save()
        else:
            data = {
                'msg': '设置评论权限失败'
            }
            return JsonResponse(data=data)
        if change == 0:
            team_relation.change = True
            team_relation.save()
        elif change == 1:
            team_relation.change = False
            team_relation.save()
        else:
            data = {
                'msg': '设置修改权限失败'
            }
            return JsonResponse(data=data)
        data = {
            'msg': '设置成功',
            'status': 0
        }
    except:
        data = {
            'msg': '设置失败',
            'status': 1
        }
    return JsonResponse(data=data)


def create_team(request):
    try:
        name = request.POST.get("name")
        tteam = Team.objects.filter(name=name)
        if tteam.exists():
            data = {
                'msg': '团队名重复',
                'status': 1,
                'id': 0
            }
            return JsonResponse(data=data)
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
            data = {
                'msg': '创建成功',
                'status': 0,
                'id': team.id
            }
    except:
        data = {
            'msg': 'wrong',
            'status': 1,
            'id': 0
        }
    return JsonResponse(data=data)


def message_list(request):
    try:
        messages = Message.objects.filter(user=request.user)
        list = []
        for message in messages:
            dic = {
                'id': message.id,
                'message': message.content
            }
            list.append(dic)
        data = {'msg': '获取消息列表成功', 'list': list, 'status': 0}
    except:
        data = {'msg': '获取失败', 'status': 1}
    return JsonResponse(data=data)


def delete_message(request):
    try:
        id = int(request.GET['id'])
        message = Message.objects.get(pk=id)
        if message:
            message.delete()
            data = {'msg': '删除成功', 'status': 0}
        else:
            data = {'msg': '删除失败', 'status': 1}
    except:
        data = {'msg': 'wrong', 'status': 1}
    return JsonResponse(data=data)
