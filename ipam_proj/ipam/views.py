from django.shortcuts import render
from rest_framework import viewsets, response, decorators
from . import serializers, models
from django.http import HttpResponse

request = HttpResponse()

# Create your views here.
class HostViewset(viewsets.ModelViewSet):
    queryset = models.Host.objects.all()
    serializer_class = serializers.HostSerializer

class RecordViewset(viewsets.ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer

class AdapterViewset(viewsets.ModelViewSet):
    queryset = models.Adapter.objects.all()
    serializer_class = serializers.AdapterSerializer

class MacViewset(viewsets.ModelViewSet):
    queryset = models.Mac.objects.all()
    serializer_class = serializers.MacSerializer

class RoleViewset(viewsets.ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer

class PreambleViewset(viewsets.ModelViewSet):
    queryset = models.Preamble.objects.all()
    serializer_class = serializers.PreambleSerializer

class SubnetViewset(viewsets.ModelViewSet):
    queryset = models.Subnet.objects.all()
    serializer_class = serializers.SubnetSerializer

class IPViewset(viewsets.ModelViewSet):
    queryset = models.IP.objects.all()
    serializer_class = serializers.IPSerializer
