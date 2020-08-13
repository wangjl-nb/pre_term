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


# 注册
def register(request):
    if request.method == 'GET':

        data = {
            "title": "注册",
        }

        return render(request, 'user/register.html', context=data)

    elif request.method == 'POST':

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        icon = request.FILES.get("icon")
        if icon == None:
            icon = "suoluetubig.jpg"
        password = make_password(password)

        user = User()
        user.u_username = username
        user.u_email = email
        user.u_password = password
        user.u_icon = icon

        user.save()
        # 设置缓存
        u_token = uuid.uuid4().hex

        print(u_token)

        cache.set(u_token, user.id, timeout=60 * 60 * 24)
        # 发送邮箱
        send_email_activate(username, email, u_token)

        return redirect(reverse('app:login'))


# 登录
def login(request):
    user_id = request.session.get('user_id')
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.filter(u_username=username).first()
    if user:
        if check_password(password, user.u_password):
            # if True:
            print("检查密码")
            if user.is_active:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.u_username
                request.session['is_manager'] = user.is_manager
                return JsonResponse(data={"msg": '登陆成功'})
            else:
                print('用户未激活')
                request.session['error_message'] = '用户未激活'
                return JsonResponse(data={"msg": '用户未激活'})
        else:
            print('密码错误')
            request.session['error_message'] = '密码错误'
            return JsonResponse(data={"msg": '密码错误'})
    else:
        print('用户名不存在')
        request.session['error_message'] = '用户不存在'
        return JsonResponse(data={"msg": '用户名错误'})


# 邮件激活
def activate(request):
    u_token = request.GET.get('u_token')

    user_id = cache.get(u_token)

    print(user_id)

    if user_id:
        cache.delete(u_token)

        user = User.objects.get(pk=user_id)

        user.is_active = True

        user.save()

        return redirect(reverse('app:login'))

    return render(request, 'user/activate_fail.html')


# 用户信息展示
def user_info(request):
    user = request.user
    data = {'u_icon': str(user.u_icon), 'u_username': user.u_username, 'u_email': user.u_email,
            'u_password': user.u_password}
    return JsonResponse(data=data)


# 登出
def logout(request):
    request.session.flush()
    return redirect(reverse('app:login'))


def change_password(request):
    new_password = request.POST['new_password']
    old_password = request.POST['old_password']
    user = request.user

    if not check_password(old_password, user.u_password):
        data = {
            "msg": "旧密码输入错误",
            "status": 1,
        }
    else:
        user.u_password = make_password(new_password)
        user.save()
        data = {
            "msg": "修改成功",
            "status": 0,
        }
    return JsonResponse(data=data)


# 搜索用户
def user_search(request):
    if request.method == 'GET':
        team_id = request.GET['team_id']
        return render(request, 'user/user_search.html', context={'team_id': team_id})
    elif request.method == 'POST':
        content = request.POST.get('search_content')
        users = User.objects.filter(Q(u_email__icontains=content) | Q(u_username__icontains=content))
        data = {
            "team_id": request.GET['team_id'],
            "users": users,
        }
        return render(request, 'user/user_search.html', context=data)


# 接收邀请函
def deal_invitation(request):
    team_id = request.GET.get('team_id')
    invitations = Team_invitation.objects.filter(team_id=team_id)
    return render(request, 'team/deal_invitation.html', context={'invitations': invitations})


# 收藏文件
def deal_collect(request):
    user = request.user
    file_id = request.GET['file_id']
    print(file_id)
    personal_collections = Personal_collection.objects.filter(user=user).filter(file_id=file_id)
    if personal_collections.exists():
        return JsonResponse(data={"msg": "已收藏"})
    else:
        personal_collections = Personal_collection()
        personal_collections.user = user
        personal_collections.file_id = file_id
        personal_collections.save()
        return JsonResponse(data={"msg": "收藏成功"})


# 修改用户名
def change_name(request):
    name = request.POST.get('u_username')
    user = request.user
    exist_user = User.objects.filter(u_username=name)
    if not exist_user.exists():
        user.u_username = name
        user.save()
        files = File.objects.filter(Q(personal_record__user=user) & Q(personal_record__is_creator=True))
        for file in files:
            file.creator = name
            file.save()
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


# 修改头像
def change_icon(request):
    user = request.user
    try:
        icon = request.FILES.get('u_icon')
        user.u_icon = icon
        user.save()
        data = {
            "msg": "修改头像成功",
            "status": 0,
        }
    except:
        data = {
            "msg": "修改头像失败",
            "status": 1,
        }
    return JsonResponse(data=data)
