from django.conf.urls import include, url
from rest_framework import routers
from api.views import *

router = routers.SimpleRouter()

router.register('profile', ProfileViewSet)
router.register('district', DistrictViewSet)
router.register('grampanchayat', GramPanchayatViewSet)
router.register('work', WorkViewSet)
router.register('employee', EmployeeViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('uploaddata/', upload_data)
]
