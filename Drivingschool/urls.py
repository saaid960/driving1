"""Drivingschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views
from home.views import home, registerpage, loginpage, logoutuser, video, index, addTodo, deleteTodo


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Apply/", views.registerpage, name="Apply"),
    path('', views.home, name="home"),
    
    
    path('todo/', views.index, name="index"),
    path('add/', addTodo),
    path('deletetodo/<int:i_id>/', deleteTodo),

    path('register/', registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),

    path('video/', views.video, name="video"),
]
urlpatterns += staticfiles_urlpatterns()
