from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import User

REQUIRE_LOGIN_JSON = [
    '/app/user_info/',
    '/app/teams_show/',
    '/app/create_file/',
    '/app/my_files_list/',
    '/app/change_file/',
    '/app/change_password/',
]
# 写路径
REQUIRE_LOGIN = [

]


class LoginMiddleware(MiddlewareMixin):
    # def process_exception(self, request, exception):
    #     print(request, exception)
    #     return redirect(reverse('app:login'))

    def process_request(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.user = user
            except:
                pass
        if request.path in REQUIRE_LOGIN_JSON:
            if user_id:
                try:
                    user = User.objects.get(pk=user_id)
                    request.user = user
                except:
                    data = {
                        'status': 302,
                        'msg': 'user not avaliable'
                    }

                    return JsonResponse(data=data)

            else:
                data = {
                    'status': 302,
                    'msg': 'user not login',
                }

                return JsonResponse(data=data)
