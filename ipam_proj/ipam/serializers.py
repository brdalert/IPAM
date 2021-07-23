from rest_framework import serializers
from . import models

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Host
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = '__all__'

class AdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adapter
        fields = '__all__'

class MacSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mac
        fields = '__all__'

class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subnet
        fields = '__all__'

class PreambleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Preamble
        fields = '__all__'

class IPSerializer(serializers.ModelSerializer):
    mac_addr = serializers.PrimaryKeyRelatedField(queryset=models.Mac.objects.all(), read_only=False)
    class Meta:
        model = models.IP
        fields = '__all__'
        depth = 5

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'

