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


# 个人文档列表
def my_files_list(request):
    type = int(request.GET['type'])
    user = request.user
    if type == 0:
        files = File.objects.filter(personal_record__user=user).filter(is_delete=False).filter(
            personal_record__is_creator=False).order_by('-id')
    elif type == 2:
        files = File.objects.filter(personal_record__user=user).filter(is_delete=False).filter(
            personal_record__is_creator=True).order_by('-id')
    elif type == 3:
        files = File.objects.filter(personal_collection__user=user).filter(is_delete=False).order_by('-id')
    else:
        files = []

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
    data = {'msg': '个人文档列表', "documentList": res}
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


# 文件信息
def file_info(request, file_id):
    file = File.objects.get(pk=file_id)
    if file.is_delete:
        data = {
            'wrong': '文档被删除',
        }
    else:
        data = {
            'file': file,
        }
    return render(request, 'file/file_info.html', context=data)


# def file_info(request):
#     try:
#         id = int(request.GET['id'])
#         file = File.objects.get(pk=id)
#         if file.is_delete == True:
#             data = {
#                 'msg':'文件已被删除'
#             }
#         else:
#             data = {
#                 'msg': '文件获取成功',
#                 'file_content': file.content
#             }
#     except:
#         data = {
#             'msg':'文件获取失败',
#         }
#     return JsonResponse(data = data)

# 文件删除
def delete_file(request):
    id = request.POST['id']
    file = File.objects.get(pk=id)
    if file.is_delete:
        return JsonResponse(data={"msg": "文件已删除", 'status': 1})
    try:
        is_team = Team_record.objects.filter(files=file)
        if is_team.exists():
            team = is_team.first().team
            level = Team_relation.objects.filter(team=team).filter(user=request.user).first().level
            if level >= 2:
                file.is_delete = True
                file.save()
                date = delete_date()
                date.file = file
                date.user = request.user
                date.save()
                return JsonResponse(data={"msg": "删除团队文档成功", 'status': 0})
            else:
                return JsonResponse(data={"msg": "删除团队文档权限不足", 'status': 1})
        else:
            is_person = Personal_record.objects.filter(files=file).filter(user=request.user)
            if is_person.exists():
                if is_person.first().is_creator:
                    file.is_delete = True
                    file.save()
                    date = delete_date()
                    date.file = file
                    date.user = request.user
                    date.save()
                    return JsonResponse(data={"msg": "删除个人文档成功", 'status': 0})
                else:
                    return JsonResponse(data={"msg": "删除个人文档权限不足", 'status': 1})
            else:
                return JsonResponse(data={"msg": "删除个人文档失败", 'status': 1})
    except:
        return JsonResponse(data={"msg": "删除个人文档失败", 'status': 1})


# 修改日志
def file_log(request):
    file_id = request.GET.get('file_id')
    file_log = File_log.objects.filter(file_id=file_id).order_by('-change_date')
    return render(request, 'file/file_log.html', context={'file_logs': file_log})


# 垃圾箱（回收站）
def personal_delete_files(request):
    user = request.user
    delete_files = File.objects.filter(Q(personal_record__user=user) & Q(personal_record__is_creator=True)).filter(
        is_delete=True)
    res = []
    for file in delete_files:
        end_date = delete_date.objects.filter(file=file).first().date
        dic = {
            "id": file.id,
            "title": file.title,
            "create_date": file.create_date,
            "delete_date": end_date,
        }
        res.append(dic)
    data = {"msg": "个人回收站列表", "list": res}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


# 恢复文档
def recover_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.is_delete = False
    file.save()
    return redirect(reverse('app:delete_files_list'))


# 文档彻底删除
def destroy_file(request):
    try:
        ids = json.loads(request.body)["ids"]
        res = []
        for id in ids:
            delete_date.objects.filter(file_id=id).delete()
            file = File.objects.get(pk=id)
            file.delete()
        return JsonResponse(data={"msg": "彻底删除文档", "status": 0})
    except:
        return JsonResponse(data={"msg": "文档删除失败", "status": 1})


# 团队文档建立
def create_team_file(request):
    if request.method == 'GET':
        team_id = request.GET.get('team_id')
        return render(request, 'team/create_team_file.html', context={'team_id': team_id})
    elif request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        file = File()
        file.title = title
        file.content = content
        file.creator = request.user.u_username
        file.save()
        team_record = Team_record()
        team_record.files = file
        team_record.team_id = request.GET.get('team_id')
        team_record.save()
        return redirect(reverse('app:file_info', args={file.id}))


# 搜索全部文档（在全部范围内搜索）
def file_search(request):
    if request.method == 'GET':
        return render(request, 'file/file_search.html')
    elif request.method == 'POST':
        content = request.POST.get('search_content')
        files = File.objects.filter(
            Q(title__icontains=content) | Q(content__icontains=content) | Q(creator__icontains=content))
        return render(request, 'file/file_search.html', context={'files': files})


# 获取模板
def get_templetes(request):
    templetes = Template.objects.all()
    print(templetes)
    res = []
    for templete in templetes:
        dic = {
            "id": templete.id,
            "content": templete.content,
            "title": templete.title,
            "score": templete.score,
            "accept_num": templete.accept_num,
            "img": str(templete.img),
        }
        res.append(dic)
    data = {
        'msg': '获取全部模板成功',
        'templetes_list': res
    }
    return JsonResponse(data=data)


# 给模板评分
def grade_templetes(request):
    id = int(request.POST['id'])
    score = float(request.POST['score'])

    templete = Template.objects.get(pk=id)
    if templete:
        if score <= 5 and score >= 0:
            if templete.accept_num == 0:
                templete.score = score
            else:
                templete.score = (templete.score + score) / templete.accept_num
            data = {
                'msg': '评分成功',
                'status': 0
            }
        else:
            data = {
                'msg': '请在0-5范围内评分',
                'status': 1
            }
    else:
        data = {
            'msg': '该模板不存在',
            'status': 1
        }
    return JsonResponse(data=data)


# 新建文档
def create_file(request):
    try:
        templete_id = int(request.POST.get('templete_id', 0))
        title = request.POST['title']
        content = request.POST['content']
        team_id = int(request.POST.get('team_id', 0))
        if templete_id == 0 and team_id == 0:
            file = File()
            file.creator = request.user.u_username
            file.save()

            personal_record = Personal_record()
            personal_record.user = request.user
            personal_record.files = file
            personal_record.save()
            data = {
                'msg': '未使用模板的个人文档创建成功',
                'status': 0,
                'id': file.id
            }
        elif templete_id != 0 and team_id == 0:
            templete = Template.objects.get(pk=templete_id)
            file = File()
            file.creator = request.user.u_username
            file.title = templete.title
            file.content = templete.content
            file.save()
            templete.accept_num = templete.accept_num + 1
            templete.save()

            personal_record = Personal_record()
            personal_record.user = request.user
            personal_record.files = file
            personal_record.save()
            data = {
                'msg': '使用模板的个人文档创建成功',
                'status': 0,
                'id': file.id
            }
        elif templete_id == 0 and team_id != 0:
            file = File()
            file.creator = request.user.u_username
            file.save()

            team_record = Team_record()
            team_record.team = Team.objects.get(pk=team_id)
            team_record.files = file
            team_record.save()
            data = {
                'msg': '未使用模板的团队文档创建成功',
                'status': 0,
                'id': file.id
            }
        elif templete_id != 0 and team_id != 0:
            templete = Template.objects.get(pk=templete_id)
            file = File()
            file.creator = request.user.u_username
            file.title = templete.title
            file.content = templete.content
            file.save()
            templete.accept_num = templete.accept_num + 1
            templete.save()

            team_record = Team_record()
            team_record.team = Team.objects.get(pk=team_id)
            team_record.files = file
            team_record.save()
            data = {
                'msg': '使用模板的团队文档创建成功',
                'status': 0,
                'id': file.id
            }
        else:
            data = {
                'msg': '新建失败',
                'status': 1
            }
    except:
        data = {
            'msg': 'wrong'
        }
    return JsonResponse(data=data)


# 个人文档给协作者授予权限
def grant_power(request):
    try:
        u_id = int(request.GET['u_id'])
        file_id = int(request.GET['id'])
        comment = int(request.GET['comment'])
        change = int(request.GET['change'])
        personal_record = Personal_record.objects.filter(user_id=u_id).filter(files_id=file_id).first()

        if comment == 1:
            personal_record.comment = True
            personal_record.save()
        elif comment == 0:
            personal_record.comment = False
            personal_record.save()
        else:
            data = {
                'msg': 'power wrong',
                'status': 1
            }
            return JsonResponse(data=data)
        if change == 1:
            personal_record.change = True
            personal_record.save()
        elif change == 0:
            personal_record.change = False
            personal_record.save()
        else:
            data = {
                'msg': 'power wrong',
                'status': 1
            }
            return JsonResponse(data=data)
        data = {
            'msg': '修改权限成功',
            'status': 0
        }
    except:
        data = {
            'msg': 'wrong',
            'status': 1
        }
    return JsonResponse(data=data)


def set_is_share(request):
    try:
        id = int(request.GET['id'])
        type = int(request.GET['type'])
        file = File.objects.get(pk=id)
        if type == 0:
            file.is_share = True
            file.save()
            data = {'msg': '开启分享权限', 'status': 0}
        elif type == 1:
            file.is_share = False
            file.save()
            data = {'msg': '关闭分享权限', 'status': 0}
        else:
            data = {
                'msg': 'wrong',
                'status': 1
            }
    except:
        data = {'msg': 'wrong', 'status': 1}
    return JsonResponse(data=data)


def cooperate_invitation(request):
    try:
        file_id = int(request.POST['id'])
        user_id = int(request.POST['u_id'])
        reason = request.POST['reason']
        personal_record = Personal_record.objects.filter(files_id=file_id).filter(user_id=user_id)
        if personal_record.exists():
            data = {
                'msg': '该用户已是该文档的协作者',
                'status': 1
            }
            return JsonResponse(data=data)
        invite = Cooperate_invitation.objects.filter(user_id=user_id).filter(file_id=file_id)
        if invite.exists():
            data = {
                'msg': '对不起，你已邀请该用户，请耐心等待',
                'status': 1
            }
            return JsonResponse(data=data)
        invite = Cooperate_invitation()
        invite.user_id = user_id
        invite.file_id = file_id
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


def coinvitation_list(request):
    try:
        cooperate_invitations = Cooperate_invitation.objects.filter(user=request.user)
        res = []
        for cooperate_invitation in cooperate_invitations:
            file = File.objects.get(pk=cooperate_invitation.file_id)
            user = User.objects.filter(personal_record__files=file).filter(personal_record__is_creator=True).first()
            dic = {
                "id": cooperate_invitation.id,
                "name": user.u_username,
                "title": file.title,
                "reason": cooperate_invitation.reason
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


def process_coinvitation(request):
    try:
        invitation_id = request.POST.get('id')
        invitation = Cooperate_invitation.objects.get(pk=invitation_id)
        type = int(request.POST['type'])
        if type == 0:
            personal_record = Personal_record()
            personal_record.user_id = invitation.user_id
            personal_record.files_id = invitation.file_id
            personal_record.is_creator = False
            personal_record.save()
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


# 修改文件
def change_file(request):
    try:
        id = request.POST.get('id')
        file = File.objects.get(pk=id)
        content = request.POST.get('content')
        title = request.POST.get('title')
        file.title = title
        file.content = content
        file.save()

        file_log = File_log()
        file_log.file = file
        file_log.user = request.user
        file_log.save()

        return JsonResponse(data={"msg": "修改成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "修改失败", "status": 1})
