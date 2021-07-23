from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.IP)
admin.site.register(models.Subnet)
admin.site.register(models.Preamble)
admin.site.register(models.Role)
admin.site.register(models.Mac)
admin.site.register(models.Adapter)
admin.site.register(models.Record)
admin.site.register(models.Host)