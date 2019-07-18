from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import api.utils.hasher as hasher


def hello(request):
    return JsonResponse({'ok': True, 'message': 'helloworld from controller!', 'path': request.path})


@csrf_exempt
def login(request):
    username = request.POST.get('user', None)
    password = str(request.POST.get('password', ''))
    hash_str = hasher.sha1_encrypt(password)
    res_compare = hasher.sha1_compare(
        password, '20eabe5d64b0e216796e834f52d61fd0b70332fc')
    response = {
        "ok": True,
        "message": 'Hello world!',
        "username": username,
        "password": password,
        "hash": hash_str,
        "res_compare": res_compare
    }
    return JsonResponse(response)
