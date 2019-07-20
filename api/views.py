from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from .models import ApiLog, Users
from .serializers import ApiLogSerializer, UserSerializer

# from django.contrib.auth.models import User


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    model = Users
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     # obj = get_object_or_404(
    #     #     queryset,
    #     #     pk=self.kwargs['pk'],
    #     # )
    #     respObj = {
    #         "ok": True
    #     }
    #     return respObj


class ApiLogList(generics.ListCreateAPIView):
    queryset = ApiLog.objects.all()
    serializer_class = ApiLogSerializer
    model = ApiLog

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        respObj = {
            "ok": True,
            "obj": obj
        }
        return respObj


@api_view(["POST"])
def test(request):
    users_list = Users.objects.all()
    id_user = request.POST.get("iduser", 0)
    a = users_list.filter(iduser=id_user)
    data = []
    for user in a:
        data.append({
            "id": user.iduser,
            "name": user.firstname,
            "lastname": user.lastname,
            "apikey": user.apikey
        })
    # import ipdb
    # ipdb.set_trace()
    return JsonResponse({"ok": True, "users": data})
