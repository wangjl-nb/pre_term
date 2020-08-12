import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
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
    user = request.user
    files = File.objects.filter(personal_record__user=user).filter(is_delete=False).order_by('-id')
    page = int(request.GET.get("page", 1))
    perpage = int(request.GET.get('perpage', 10))
    paginator = Paginator(files, perpage)

    page_object = paginator.page(page)
    data = {'msg': '个人文档列表', 'files': page_object, "page_range": paginator.page_range}
    return render(request, 'file/my_files_list.html', context=data)


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
            return render(request, 'team/teaminfo.html', context={"team": team})


def user_info_change(request):
    username = request.POST.get("username")
    icon = request.FILES.get("icon")

    user = request.user

    user.u_username = username
    if icon != None:
        user.u_icon = icon
    user.save()
    return HttpResponse('用户信息修改成功')


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
    relation = Team.objects.filter(user_id=user_id).filter(team_id=team_id)
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
    return render(request,'team/deal_application.html',context={'applications':applications})


def process_application(request):
    apply_id = request.GET.get('applyid')
    application = Team_application.objects.get(pk=apply_id)
    if request.GET.get('type') == 'agree':
        team = Team.objects.get(pk=application.team_id)
        team.number_num = team.number_num+1
        team.save()
        team_relation = Team_relation()
        team_relation.level=1
        team_relation.team=team
        team_relation.user=application.user
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