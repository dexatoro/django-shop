from django.contrib import admin
from django.urls import path
from crm.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
