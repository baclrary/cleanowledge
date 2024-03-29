from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "first_name", "middle_name", "last_name")

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
