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
    if user_id:
        return redirect(reverse('app:user_info'))
        # return HttpResponseRedirect(reverse('web:one_group',args=[7]))
    else:
        if request.method == "GET":
            error_message = request.session.get('error_message')
            data = {
                "title": "登录",
            }
            if error_message:
                del request.session['error_message']
                data['error_message'] = error_message
            return render(request, 'user/login.html', context=data)
        elif request.method == "POST":

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
            print('用户名不存在')
            request.session['error_message'] = '用户不存在'
            return redirect(reverse('app:login'))
        else:
            return redirect(reverse('app:login'))


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
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    data = {'icon': user.u_icon, 'username': user.u_username, 'email': user.u_email}
    return render(request, 'user/info.html', context=data)


# 登出
def logout(request):
    request.session.flush()
    return redirect(reverse('app:login'))


def user_info_change(request):
    username = request.POST.get("username")
    icon = request.FILES.get("icon")

    user = request.user

    user.u_username = username
    if icon != None:
        user.u_icon = icon
    if not check_password(request.POST.get("oldpwd"), user.u_password):
        return HttpResponse("原密码输入有误")
    if request.POST.get("newpwd1") != request.POST.get("newpwd2"):
        return HttpResponse("两次密码输入不一致")
    user.u_password = make_password(request.POST.get("newpwd1"))

    user.save()
    return HttpResponse('用户信息修改成功')


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
