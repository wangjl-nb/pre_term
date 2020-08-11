import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import *
from App.views_helper import send_email_activate


def index(request):
    return HttpResponse('Hello World')


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

        # user = User.objects.filter(u_email=email)
        # if user.exists():
        #     return redirect(reverse("Web:register"))

        # password = hash_str(password)
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
                        print("登陆成功")
                        return redirect(reverse('app:user_info'))
                    else:
                        print('用户未激活')
                        request.session['error_message'] = '用户未激活'
                        return redirect(reverse('app:login'))
                else:
                    print('密码错误')
                    request.session['error_message'] = '密码错误'
                    return redirect(reverse('app:login'))
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
    return render(request, 'team/teams_info.html', context=data)


# 团队信息展示
def team_info(request):
    team_id = request.GET.get('team_id', 4)
    team = Team.objects.get(pk=team_id)
    # data = {'name': team.name, 'create_date': team.create_date, 'number_num': team.number_num,
    #         'describe': team.describe, 'icon': team.icon}
    return render(request, 'team/teaminfo.html', context={'team': team})


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


def my_files_list(request):
    user = request.user
    files = File.objects.filter(personal_record__user=user).filter(is_delete=False).order_by('-id')
    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(files, perpage)

    page_object = paginator.page(page)
    data = {'msg': '个人文档列表', 'files': page_object, "page_range": paginator.page_range}
    return render(request, 'file/my_files_list.html', context=data)


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


def delete_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.is_delete = True
    file.save()
    return redirect(reverse('app:my_files_list'))


def file_log(request):
    file_id = request.GET.get('file_id')
    file_log = File_log.objects.filter(file_id=file_id).order_by('-change_date')
    return render(request, 'file/file_log.html', context={'file_logs': file_log})
