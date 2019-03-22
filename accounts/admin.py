from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib import admin
from .filter import UserDateJoinedFilter


admin.site.unregister(User)
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'date_joined', UserDateJoinedFilter)
