from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('post_list/', views.post_list, name="post_list"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/draft/', views.post_draft_list, name="post_draft_list"),
    path('post/<int:post_id>/', views.post_detail, name="post_detail"),
    path('post/<int:post_id>/publish/', views.post_publish, name="post_publish"),
    path('post/<int:post_id>/edit/', views.post_edit, name="post_edit"),
    path('post/<int:post_id>/delete/', views.post_delete, name="post_delete"),
]
