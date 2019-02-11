from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('post_list/', views.post_list, name="post_list"),
    path('<post_id>/', views.post_detail, name="post_detail"),
]
