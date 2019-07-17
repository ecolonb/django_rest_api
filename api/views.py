from rest_framework import generics, permissions
from .serializers import UserSerializer, ApiLogSerializer
from .models import Users, ApiLog
from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        # obj = get_object_or_404(
        #     queryset,
        #     pk=self.kwargs['pk'],
        # )
        respObj = {
            "ok": True
        }
        return respObj


class ApiLogList(generics.ListCreateAPIView):
    queryset = ApiLog.objects.all()
    serializer_class = ApiLogSerializer

    def get_object(self):
        queryset = self.get_queryset()
        # obj = get_object_or_404(
        #     queryset,
        #     pk=self.kwargs['pk'],
        # )
        respObj = {
            "ok": True
        }
        return respObj
