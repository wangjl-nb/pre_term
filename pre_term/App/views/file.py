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


def create_file(request):
    if request.method == 'GET':
        return render(request, 'file/create_file.html')
    elif request.method == 'POST':
        content = request.POST.get('content')
        title = request.POST.get('title')
        file = File()
        file.title = title
        file.content = content
        file.creator = request.user.u_username
        file.save()
        personal_record = Personal_record()
        personal_record.user = request.user
        personal_record.files = file
        personal_record.save()
        return redirect(reverse('app:file_info', args={file.id}))


# 修改文件
def change_file(request, file_id):
    if request.method == 'GET':
        file = File.objects.get(pk=file_id)
        return render(request, 'file/change_file.html', context={'file': file})
    elif request.method == 'POST':
        file = File.objects.get(pk=file_id)
        content = request.POST.get('content')
        title = request.POST.get('title')
        file.title = title
        file.content = content
        file.save()

        file_log = File_log()
        file_log.file = file
        file_log.user = request.user
        file_log.save()

        return redirect(reverse('app:file_info', args={file.id}))


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
    # files = File.objects.all().order_by('-id')

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


# 文件删除
def delete_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.is_delete = True
    file.save()
    deletedate = delete_date()
    deletedate.file = file
    deletedate.user = request.user
    deletedate.save()

    return redirect(reverse('app:my_files_list'))


# 修改日志
def file_log(request):
    file_id = request.GET.get('file_id')
    file_log = File_log.objects.filter(file_id=file_id).order_by('-change_date')
    return render(request, 'file/file_log.html', context={'file_logs': file_log})


# 垃圾箱（回收站）
def delete_files_list(request):
    user = request.user
    delete_files = File.objects.filter(personal_record__user=user).filter(is_delete=True)
    return render(request, 'file/delete_files_list.html', context={'delete_files': delete_files})


# 恢复文档
def recover_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.is_delete = False
    file.save()
    return redirect(reverse('app:delete_files_list'))


# 文档彻底删除
def destroy_file(request):
    file_id = request.GET.get('file_id')
    file = File.objects.get(pk=file_id)
    file.delete()
    return redirect(reverse('app:delete_files_list'))


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
