from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from profiles_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', employeeList.as_view()),
]
