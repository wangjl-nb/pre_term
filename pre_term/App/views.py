import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import *
from App.views_helper import send_email_activate


def index(request):
    return HttpResponse('Hello World')


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

        u_token = uuid.uuid4().hex

        print(u_token)

        cache.set(u_token, user.id, timeout=60 * 60 * 24)

        send_email_activate(username, email, u_token)

        return redirect(reverse('app:login'))


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


def user_info(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    data={}
    data['icon']=user.u_icon
    data['username']=user.u_username
    data['email']=user.u_email
    return render(request,'user/info.html',context=data)


def logout(request):
    request.session.flush()
    return redirect(reverse('app:login'))