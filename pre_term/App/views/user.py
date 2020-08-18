import json
import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.urls import reverse
from App.models import *
from App.views_helper import send_email_activate


# 注册
def register(request):
    try:
        username = request.POST.get("u_username")
        email = request.POST.get("u_email")
        password = request.POST.get("u_password")
        icon = request.FILES.get("u_icon")
        if icon == None:
            icon = "suoluetubig.jpg"
        password = make_password(password)

        user = User()
        user.u_username = username
        user.u_email = email
        user.u_password = password
        user.u_icon = icon
        user.is_active=True

        user.save()
        # 设置缓存
        # u_token = uuid.uuid4().hex
        #
        # print(u_token)

        # cache.set(u_token, user.id, timeout=60 * 60 * 24)
        # 发送邮箱
        # send_email_activate(username, email, u_token)

        return JsonResponse(data={"msg": "注册成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "注册失败", "status": 1})


# 登录
def login(request):
    username = request.POST.get("u_username")
    password = request.POST.get("u_password")
    print(username)
    user = User.objects.filter(u_username=username).first()
    if user:
        if check_password(password, user.u_password):
            # if True:
            print("检查密码")
            if user.is_active:
                request.session['user_id'] = user.id
                request.session['user_name'] = user.u_username
                request.session['is_manager'] = user.is_manager
                return JsonResponse(data={"msg": '登陆成功', "status": 0})
            else:
                print('用户未激活')
                request.session['error_message'] = '用户未激活'
                return JsonResponse(data={"msg": '用户未激活', "status": 1})
        else:
            print('密码错误')
            request.session['error_message'] = '密码错误'
            return JsonResponse(data={"msg": '密码错误', "status": 1})
    else:
        print('用户名不存在')
        request.session['error_message'] = '用户不存在'
        return JsonResponse(data={"msg": '用户名错误', "status": 1})


# 邮件激活
# def activate(request):
#     u_token = request.GET.get('u_token')
#
#     user_id = cache.get(u_token)
#
#     print(user_id)
#
#     if user_id:
#         cache.delete(u_token)
#
#         user = User.objects.get(pk=user_id)
#
#         user.is_active = True
#
#         user.save()
#
#         return HttpResponseRedirect("/login")
#
#     return JsonResponse(data={"msg": "用户激活失败", "status": 1})


# 用户信息展示
def user_info(request):
    user = request.user
    data = {'u_icon': str(user.u_icon), 'u_username': user.u_username, 'u_email': user.u_email,
            'u_password': user.u_password}
    return JsonResponse(data=data)


# 登出
def logout(request):
    try:
        request.session.flush()
        return JsonResponse(data={"msg": "用户登出成功", "status": 0})
    except:
        return JsonResponse(data={"msg": "用户登出失败", "status": 1})


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


# 用户搜索
def search_person(request):
    key = request.POST['key']
    users = User.objects.filter(Q(u_email__icontains=key) | Q(u_username__icontains=key)).order_by("id")
    res = []
    for user in users:
        if user != request.user:
            dic = {
                "id": user.id,
                "u_icon": str(user.u_icon),
                "u_username": user.u_username,
            }
            res.append(dic)
    data = {'msg': '用户搜索列表', "list": res}
    return HttpResponse(json.dumps(data), content_type='application/json')


def is_login(request):
    user_id = request.session.get("user_id")
    if user_id:
        user = User.objects.get(pk=user_id)
        if user.is_manager:
            return JsonResponse(data={"type": 2, "user_id": user.id})
        else:
            return JsonResponse(data={"type": 1, "user_id": user.id})
    return JsonResponse(data={"type": 0})


# 收藏文件
def deal_collect(request):
    try:
        user = request.user
        file_id = int(request.POST['id'])
        type = int(request.POST['type'])
        if type == 0:
            personal_collections = Personal_collection.objects.filter(user=user).filter(files_id=file_id)
            if personal_collections.exists():
                data = {'msg': '已收藏', 'status': 1}
            else:
                personal_collections = Personal_collection()
                personal_collections.user = user
                personal_collections.files_id = file_id
                personal_collections.save()
                data = {'msg': '收藏成功', 'status': 0}
        elif type == 1:
            personal_collections = Personal_collection.objects.filter(user=user).filter(files_id=file_id).first()
            print(personal_collections)
            if not personal_collections:
                data = {'msg': '未收藏', 'status': 1}
            else:
                personal_collections.delete()
                data = {'msg': '取消收藏成功', 'status': 0}
    except:
        data = {'msg': 'wrong', 'status': 1}
    return JsonResponse(data=data)
