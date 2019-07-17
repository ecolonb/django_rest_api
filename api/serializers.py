from .models import Users, ApiLog
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ('iduser', 'iddiscount', 'miniumiddiscount', 'discountupdatedat', 'iddealer', 'idusergroup', 'username', 'email', 'password', 'firstname', 'lastname', 'rfc', 'company', 'type', 'credit',
                  'activated', 'ispro', 'isvalidpro', 'proterms', 'thermallabel', 'apikey', 'changepasswordtoken', 'created', 'modified', 'phone', 'remember_token', 'id_conekta_client', 'lockeddiscount')


class ApiLogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ApiLog
        fields = ('id', 'iduser', 'request', 'response',
                  'services', 'created_at', 'updated_at')
