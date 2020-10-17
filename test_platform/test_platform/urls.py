"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app_person import views as person_views
from app_manage import views as manage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',person_views.hello),
    # 账户管理
    path("",person_views.login),
    path('login/',person_views.login),
    path('logout/',person_views.logout),
    # 项目管理
    path('manage/',manage_views.manage),
    path('project/',include('app_manage.urls')),
]