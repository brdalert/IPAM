from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model):
    host_name = models.CharField(default='Host', max_length=256)
    def __str__(self):
        return self.host_name + '\n id: ' + str(self.id)

class Record(models.Model):
    RECORD_TYPES = (('A', 'A'), ('AAAA', 'AAAA'), ('ALIAS', 'ALIAS'), ('cname', 'cname'),
                    ('MX', 'MX'), ('NS', 'NS'), ('PTR', "PTR"), ('SOA', 'SOA'))
    record_type = models.CharField(choices=RECORD_TYPES, max_length=8)
    host = models.ForeignKey(Host, related_name='host', on_delete=models.CASCADE)
    def __str__(self):
        return self.record_type + '\n id: ' + str(self.id)

class Adapter(models.Model):
    host = models.ForeignKey(Host, related_name='adapter', on_delete=models.CASCADE)
    adapter_name = models.CharField(max_length=50, default='Adapter')
    def __str__(self):
        return self.adapter_name + '\n id: ' + str(self.id)

class Mac(models.Model):
    adapter = models.OneToOneField(Adapter, related_name='mac',on_delete=models.CASCADE)
    mac = models.CharField(max_length=18)
    def __str__(self):
        return self.mac + '\n id: ' + str(self.id)

class Role(models.Model):
    user = models.ManyToManyField(User)
    role_name = models.CharField(max_length=50, default='Role')
    def __str__(self):
        return self.role_name + '\n id: ' + str(self.id)

class Preamble(models.Model):
    pa_subnet_name = models.CharField(max_length=50, default='pre')
    ttl = models.CharField(max_length=50)
    retry = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    name_server = models.CharField(max_length=50)
    email_addr = models.CharField(max_length=20)
    expiry = models.CharField(max_length=50)
    refresh = models.CharField(max_length=50)
    nxdomain_ttl = models.CharField(max_length=50)
    def __str__(self):
        return self.pa_subnet_name + '\n id: ' + str(self.id)

class Subnet(models.Model):
    preamble = models.OneToOneField(Preamble, related_name='subnet',on_delete=models.CASCADE)
    role = models.OneToOneField(Role, related_name='subnet', on_delete=models.SET_NULL, blank=True, null=True)
    subnet_name = models.CharField(max_length=128, default='Sub')
    def __str__(self):
        return self.subnet_name + '\n id: ' + str(self.id)

class IP(models.Model):
    mac_addr = models.OneToOneField(Mac, related_name='IP', on_delete=models.SET_NULL, blank=True, null=True)
    subnet = models.ForeignKey(Subnet, related_name='IP', on_delete=models.DO_NOTHING)
    ipv4 = models.CharField(max_length=12, blank=True, null=True)
    ipv6 = models.CharField(max_length=40, blank=True, null=True)
    def __str__(self):
        if self.ipv4 is not None:
            return self.ipv4 + '\n id: ' + str(self.id)
        if self.ipv6 is not None:
            return self.ipv6 + '\n id: ' + str(self.id)
