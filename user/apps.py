from django.contrib.auth.admin import UserAdmin

from user import admin
from .models import User


@admin.register(User)
class CustomUsersAdmin(UserAdmin):
    pass
