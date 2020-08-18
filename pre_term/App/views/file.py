import datetime
import json
import uuid
import decimal
from audioop import avg

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q, Avg
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
        records = Personal_record.objects.filter(user=user).order_by('-id')
    elif type == 1:
        records = File_log.objects.filter(user=user).order_by('-change_date')
    elif type == 2:
        records = Personal_record.objects.filter(user=user).filter(is_creator=True).order_by('-id')
    elif type == 3:
        records = Personal_collection.objects.filter(user=user).order_by('-id')
    else:
        records = []

    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(records, perpage)

    page_object = paginator.page(page)
    res = []
    for record in page_object:
        try:
            file = record.files
        except:
            file = record.file
        if not file.is_delete:
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
    data = {'msg': '个人文档列表', "documentList": res, "pages": paginator.num_pages}
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
def file_info(request):
    file_id = request.GET['id']
    file = File.objects.get(pk=file_id)
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse(data={"type": -2})
    user = request.user
    record = Personal_record.objects.filter(files=file)
    data = {}
    data['allow_Share'] = 0 if file.is_share else 1
    if record.exists():
        data['team_id'] = -1
        record = record.filter(user=user)
        data['is_team'] = 0
        collection = Personal_collection.objects.filter(files=file).filter(user=user)
        if collection.exists():
            data['star'] = 0
        else:
            data['star'] = 1
        if not record.exists():
            data['type'] = -1
            data['change'] = 1
            data['comment'] = 1
        else:
            if record.first().is_creator:
                data['type'] = 1
                data['change'] = 0
                data['comment'] = 0
            else:
                data['type'] = 0
                data['change'] = 0 if record.first().change else 1
                data['comment'] = 0 if record.first().comment else 1
        records = Personal_record.objects.filter(files=file)
        list = []
        for record in records:
            if not record.is_creator:
                user = record.user
                dic = {
                    "id": user.id,
                    "u_username": user.u_username,
                    "u_icon": str(user.u_icon),
                    "change": 0 if record.change else 1,
                    "comment": 0 if record.comment else 1,
                }
                list.append(dic)
        data["list"] = list
    else:
        data['star'] = -1
        data['is_team'] = 0
        data['list'] = []
        team = Team_record.objects.filter(files=file).first().team
        relation = Team_relation.objects.filter(team=team).filter(user=user)
        data['team_id'] = team.id
        if relation.exists():
            relation = relation.first()
            if relation.level >= 2:
                data['type'] = 1
                data['change'] = 0
                data['comment'] = 0
            else:
                data['type'] = 0
                data['change'] = 0 if relation.change else 1
                data['comment'] = 0 if relation.comment else 1
        else:
            data['type'] = -1
            data['change'] = 1
            data['comment'] = 1
    data['create_date'] = file.create_date
    data['creator'] = file.creator
    data['title'] = file.title
    data['content'] = file.content
    if file.is_delete:
        data['is_delete'] = 1
    else:
        data['is_delete'] = 0
    list = []
    comments = Comment.objects.filter(file=file)
    for comment in comments:
        dic = {
            'id': comment.id,
            'time': comment.time,
            'content': comment.content,
            'u_username': comment.user.u_username,
        }
        list.append(dic)
    data['comments'] = list
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


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
def recover_file(request):
    try:
        ids = json.loads(request.body)["ids"]
        res = []
        for id in ids:
            delete_date.objects.filter(file_id=id).delete()
            file = File.objects.get(pk=id)
            file.is_delete = False
            file.save()
        return JsonResponse(data={"msg": "文档恢复成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "文档恢复失败", "status": 1})


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


# 获取模板
def get_templetes(request):
    templetes = Template.objects.all()
    print(templetes)
    res = []
    for templete in templetes:
        grade = Templete_grade.objects.filter(user=request.user).filter(templete=templete)
        if grade.exists():
            myscore = grade.first().score
        else:
            myscore = -1
        dic = {
            "id": templete.id,
            "content": templete.content,
            "title": templete.title,
            "score": templete.score,
            "accept_num": templete.accept_num,
            "img": str(templete.img),
            "myscore": myscore,
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
    score = decimal.Decimal(request.POST.get('score'))
    templete_grade = Templete_grade.objects.filter(templete_id=id).filter(user=request.user)
    if templete_grade:
        data = {'msg': '您已评分', 'status': 1}
        return JsonResponse(data=data)
    templete = Template.objects.get(pk=id)
    if templete:
        if score <= 5 and score >= 0:
            templete_grade = Templete_grade()
            templete_grade.score = score
            templete_grade.templete_id = id
            templete_grade.user = request.user
            templete_grade.save()
            dict = Templete_grade.objects.filter(templete_id=id).aggregate(Avg('score'))

            templete.score = dict['score__avg']
            templete.save()
            # templete.score = avg(templete_grades.score)
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
        team_id = int(request.POST.get('team_id', 0))
        templete_id = int(request.POST.get('templete_id', 0))
        if team_id == 0:
            file = File()
            file.creator = request.user.u_username
            if templete_id != 0:
                templete = Template.objects.get(pk=templete_id)
                title = templete.title
                content = templete.content
                templete.accept_num = templete.accept_num + 1
                templete.save()
            else:
                title = "空白文档"
                content = ""
            file.title = title
            file.content = content
            file.save()

            personal_record = Personal_record()
            personal_record.user = request.user
            personal_record.files = file
            personal_record.save()
            data = {
                'msg': '个人文档创建成功',
                'status': 0,
                'id': file.id
            }
        elif team_id != 0:
            file = File()
            file.creator = request.user.u_username
            if templete_id != 0:
                templete = Template.objects.get(pk=templete_id)
                title = templete.title
                content = templete.content
                templete.accept_num = templete.accept_num + 1
                templete.save()
            else:
                title = "空白文档"
                content = ""
            file.title = title
            file.content = content
            file.save()

            team_record = Team_record()
            team_record.team = Team.objects.get(pk=team_id)
            team_record.files = file
            team_record.save()
            data = {
                'msg': '团队文档创建成功',
                'status': 0,
                'id': file.id
            }
        else:
            data = {
                'msg': '新建失败',
                'status': 1
            }
        file_log = File_log()
        file_log.file = file
        file_log.user = request.user
        file_log.save()
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
            personal_record.comment = False
            personal_record.save()
        elif comment == 0:
            personal_record.comment = True
            personal_record.save()
        else:
            data = {
                'msg': 'power wrong',
                'status': 1
            }
            return JsonResponse(data=data)
        if change == 1:
            personal_record.change = False
            personal_record.save()
        elif change == 0:
            personal_record.change = True
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
    # try:
    invitation_id = request.POST.get('id')
    invitation = Cooperate_invitation.objects.get(pk=invitation_id)
    type = int(request.POST['type'])
    message = Message()
    user = User.objects.get(pk=invitation.user_id)
    file = File.objects.get(pk=invitation.file_id)
    record = Personal_record.objects.filter(files=file).filter(is_creator=True).first()
    if type == 0:
        personal_record = Personal_record()
        personal_record.user_id = invitation.user_id
        personal_record.files_id = invitation.file_id
        personal_record.is_creator = False
        personal_record.save()
        data = {
            "msg": "已接受邀请",
            'status': 0
        }
        message.content = user.u_username + '接受了你的邀请成为文档' + file.title + '的协作者'
    else:
        data = {
            "msg": "已拒绝邀请",
            'status': 1
        }
        message.content = user.u_username + '拒绝了成为文档' + file.title + '的协作者的邀请'
    message.user = User.objects.get(pk=record.user_id)
    message.save()
    invitation.delete()
    # except:
    #     data = {
    #         'msg': 'wrong',
    #         'status': 1
    #     }
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
        file_log = File_log.objects.filter(file=file).filter(user=request.user)
        if file_log.exists():
            file_log.delete()
        file_log = File_log()
        file_log.file = file
        file_log.user = request.user
        file_log.save()

        return JsonResponse(data={"msg": "修改成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "修改失败", "status": 1})


def submit_comment(request):
    try:
        file_id = int(request.POST['id'])
        content = request.POST['content']
        comment = Comment()
        comment.file_id = file_id
        comment.content = content
        comment.user = request.user
        comment.save()

        comment_reminder = Comment_reminder()
        comment_reminder.comment = comment
        comment_reminder.user_id = Personal_record.objects.filter(files_id=file_id).filter(
            is_creator=True).first().user_id
        comment_reminder.save()
        data = {
            'msg': '评论成功',
            'status': 0,
            'id': comment.id,
            'u_username': request.user.u_username,
            'time': comment.time
        }
    except:
        data = {'msg': '评论失败', 'status': 1}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


# 收到评论提醒
def comment_reminder(request):
    try:
        comment_reminders = Comment_reminder.objects.filter(user=request.user)
        list = []
        for comment_reminder in comment_reminders:
            comment = Comment.objects.get(pk=comment_reminder.comment_id)
            file = File.objects.get(pk=comment.file_id)
            user = User.objects.get(pk=comment.user_id)
            dic = {
                'title': file.title,
                'u_username': user.u_username,
                'date': comment.time
            }
            list.append(dic)
        data = {'msg': '获取评论提醒成功', 'list': list}
    except:
        data = {'msg': '获取评论提醒失败'}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


def file_search(request):
    try:
        content = request.POST.get('key')
        list = []
        personal_records = Personal_record.objects.all()
        for personal_record in personal_records:
            list.append(personal_record.files_id)
        files = File.objects.filter(
            Q(title__icontains=content) | Q(content__icontains=content) | Q(creator__icontains=content))
        ids = []
        for file in files:
            if file.id in list:
                file_log = File_log.objects.filter(file_id=file.id).order_by("-id").first()
                if file_log:
                    change_date = file_log.change_date
                    u_username = file_log.user.u_username
                else:
                    change_date = file.create_date
                    u_username = file.creator
                dic = {
                    "file_id": file.id,
                    "title": file.title,
                    "creator": file.creator,
                    "create_date": file.create_date,
                    "change_date": change_date,
                    "u_username": u_username
                }
                ids.append(dic)
        data = {
            'msg': '搜索成功',
            'list': ids
        }
    except:
        data = {'msg': '搜索失败'}
    return JsonResponse(data=data)


def file_content(request):
    try:
        file = File.objects.get(pk=request.GET['id'])
        change_power = Change_power.objects.filter(file=file).first()
        data = {}
        if change_power:
            if change_power.user == request.user:
                data['power'] = 0
                data['status'] = 0
            else:
                data['power'] = 1
                data['status'] = 1
        else:
            data['power'] = 2
            data['status'] = 0
        data['title'] = file.title
        data['content'] = file.content
        data['msg'] = '获取成功'
    except:
        data = {
            'msg': 'wrong',
            "status": 1
        }
    return JsonResponse(data=data)


# 收到评论提醒
def comment_reminder(request):
    try:
        comment_reminders = Comment_reminder.objects.filter(user=request.user)
        list = []
        for comment_reminder in comment_reminders:
            comment = Comment.objects.get(pk=comment_reminder.comment_id)
            file = File.objects.get(pk=comment.file_id)
            user = User.objects.get(pk=comment.user_id)
            dic = {
                'id': comment_reminder.id,
                'title': file.title,
                'u_username': user.u_username,
                'date': comment.time
            }
            list.append(dic)
        data = {'msg': '获取评论提醒成功', 'list': list}
    except:
        data = {'msg': '获取评论提醒失败'}
    return HttpResponse(json.dumps(data, cls=DateEncoder), content_type='application/json')


def delete_comment_reminder(request):
    try:
        id = int(request.GET['id'])
        comment_reminder = Comment_reminder.objects.get(pk=id)
        if comment_reminder != None:
            comment_reminder.delete()
            data = {'msg': '删除成功', 'status': 0}
        else:
            data = {'msg': '删除失败', 'status': 1}
    except:
        data = {'msg': '删除失败', 'status': 1}
    return JsonResponse(data=data)


def template_content(request):
    try:
        template = Template.objects.get(pk=int(request.GET['id']))
        data = {
            "title": template.title,
            "content": template.content,
            "status": 0,
        }
    except:
        data = {
            "status": 1,
        }
    return JsonResponse(data=data)


def get_change_power(request):
    id = int(request.GET['id'])
    change_power = Change_power.objects.filter(file_id=id)
    if change_power.exists():
        if change_power.first().user != request.user:
            data = {
                'msg': '获取修改权限失败',
                'status': 1,
            }
            return JsonResponse(data=data)
        else:
            data = {
                'msg': '您已有权限',
                'status': 0,
            }
            return JsonResponse(data=data)
    else:
        change_power = Change_power()
        change_power.user = request.user
        change_power.file_id = id
        change_power.save()
        data = {'msg': '获取修改权限成功', 'status': 0}
    return JsonResponse(data=data)


def abandon_change_power(request):
    id = int(request.GET['id'])
    change_power = Change_power.objects.filter(file_id=id).filter(user=request.user)
    if change_power.exists():
        change_power.delete()
        data = {'msg': '放弃修改权限成功', 'status': 0}
    else:
        data = {'msg': '本人无修改权限，放弃失败', 'status': 1}
    return JsonResponse(data=data)


def delete_comment(request):
    try:
        comment_id = request.GET['id']
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
        data = {
            "status": 0,
            "msg": "删除成功",
        }
    except:
        data = {
            "status": 1,
            "msg": "删除失败",
        }
    return JsonResponse(data=data)
