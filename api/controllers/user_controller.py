from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import api.utils.hasher as hasher
from api.models import Users


def hello(request):
    return JsonResponse({'ok': True, 'message': 'helloworld from controller!', 'path': request.path})


# @csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.POST.get('user', None)
    password = str(request.POST.get('password', ''))
    res_compare = hasher.sha1_compare(
        password, '20eabe5d64b0e216796e834f52d61fd0b70332fc')
    password = hasher.sha1_encrypt(password)
    users = Users.objects.all()
    user = users.filter(password=password, email=username)
    apikey = None
    for user in user:
        apikey = user.apikey
    # import ipdb
    # ipdb.set_trace()
    response = {
        "ok": True,
        "message": 'Hello world!',
        "username": username,
        "password": password,
        "res_compare": res_compare,
        "apikey": apikey
    }
    return JsonResponse(response)
