from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post, Comment)
class PostAdmin(admin.ModelAdmin):
    pass
