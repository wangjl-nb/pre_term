from .file import *
from .user import *
from .team import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def index(request):
    # type = request.POST.get('type')
    # return JsonResponse(data={'date': "这是数据", "type": type})
    return HttpResponseRedirect("/login")


