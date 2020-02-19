from django.contrib import admin
from django.urls import path, include
from department import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('department.urls')),
]
