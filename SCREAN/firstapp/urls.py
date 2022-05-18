from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name='home'),
    path('reg/', views.RegisterFormView.as_view()),
    path('NOBLUR/', views.password),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('logaut/', views.Log),
    path('DEL/', views.DELETE),
    path('LICH/', views.TIR)
]