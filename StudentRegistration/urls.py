"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'StudentRegistration'

urlpatterns = [
    url(r'^login/$', views.UserLogin, name='login_user'),
    url(r'^logout/$', views.UserLogout, name='logout_user'),
    url(r'^registerUser/$', views.UserRegister, name='register_user'),
    url(r'^addStudentInfo/$', views.add_StudentInfo, name='add_StudentInfo'),
    path('deleteStudentDetails/<int:pk>/', views.delete_StudentDetails, name='delete_StudentDetails'),
    path('editStudentDetails/<int:pk>/', views.edit_StudentDetails, name='edit_StudentDetails'),
    url(r'^searchStudentDetails/$', views.search_StudentDetails, name='search_StudentDetails'),
]
