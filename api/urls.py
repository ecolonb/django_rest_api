
#from urllib import request

from django.urls import path

from . import views

from api.controllers import user_controller


urlpatterns = [
    path('users', views.UsersList.as_view()),
    path('log', views.ApiLogList.as_view()),
    path('hello', user_controller.hello),
    path('test', views.test),
    path('users_list', user_controller.allUsers),
    path('login', user_controller.login)
]
