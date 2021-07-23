
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import ipam.views as views

router = DefaultRouter()
router.register('listallips', views.IPViewset)
router.register('createhost', views.HostViewset)
router.register('createrecord', views.RecordViewset)
router.register('createadapter', views.AdapterViewset)
router.register('createmac', views.MacViewset)
router.register('updateip', views.IPViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
