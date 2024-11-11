"""LiverDisease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from admins import views as admins
from django.contrib import admin
from django.urls import path
from users import views as usr

from MedicalAssistance import views as mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),

    ### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("UserVideoProcess/", usr.UserVideoProcess, name="UserVideoProcess"),
    path("myTest/", usr.myTest, name="myTest"),
    path("user_view_profile/", usr.user_view_profile, name="user_view_profile"),
    path("UserViewResults/", usr.UserViewResults, name="UserViewResults"),

    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    path("AdminVideoProcess/", admins.AdminVideoProcess, name="AdminVideoProcess"),
    path("AdminViewResults/", admins.AdminViewResults, name="AdminViewResults"),
    path("delete_result/", admins.delete_result, name="delete_result"),
    path("AddUser/", admins.AddUser, name="AddUser"),
    path("AdminDeleteUsers/", admins.AdminDeleteUsers, name="AdminDeleteUsers"),

]
