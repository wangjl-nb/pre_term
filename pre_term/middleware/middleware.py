from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import User

REQUIRE_LOGIN_JSON = [
]
# 写路径
REQUIRE_LOGIN = [
    '/app/user_info/',
    '/app/teams_show/',
    '/app/create_file/',
    '/app/my_files_list/',
    '/app/change_file/'
]


class LoginMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        print(request, exception)
        return redirect(reverse('app:login'))

    def process_request(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.user = user
            except:
                return redirect(reverse('app:login'))
        if request.path in REQUIRE_LOGIN:
            if not user_id:
                return redirect(reverse('app:login'))

        #     user_id = request.session.get('user_id')
        #     if user_id:
        #         request.user = User.objects.get(pk=user_id)
        #
        #     if request.path in REQUIRE_LOGIN_JSON:
        #
        #         user_id = request.session.get('user_id')
        #
        #         if user_id:
        #             try:
        #                 user = User.objects.get(pk=user_id)
        #
        #                 request.user = user
        #             except:
        #                 # return redirect(reverse('axf:login'))
        #                 data = {
        #                     'status': 302,
        #                     'msg': 'user not avaliable'
        #                 }
        #
        #                 return JsonResponse(data=data)
        #         else:
        #             # return redirect(reverse('axf:login'))
        #             data = {
        #                 'status': 302,
        #                 'msg': 'user not login',
        #             }
        #
        #             return JsonResponse(data=data)
