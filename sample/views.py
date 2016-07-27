from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import Route, DynamicDetailRoute, SimpleRouter
from rest_framework.decorators import detail_route
from sample.models import LicenseToken

# Create your views here.

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'pk')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LicenseTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LicenseToken
        fields = ('serial_no', 'access_token', 'pk')

# ViewSets define the view behavior.
class LicenseTokenViewSet(viewsets.ModelViewSet):
    queryset = LicenseToken.objects.all()
    serializer_class = LicenseTokenSerializer

def lic_list(request):
	return HttpResponse("hello")
