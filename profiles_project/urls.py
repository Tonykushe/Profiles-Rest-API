from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from profiles_api.views import *
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employee-viewset', EmployeeViewSet, base_name='employee-viewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', employeeList.as_view()),
    path('', include(router.urls))
]
