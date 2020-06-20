from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import ugettext as _
# Gotta change some class variables to support our custom user models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']  # order them by id
    list_display = ['name', 'email']  # list them by name and email
    # add field sets to match our custom user models
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', )}),
        (
            _('Permissions'), {'fields': (
                'is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': (
            'email', 'password1', 'password2')}),
    )


# finally register with our app
admin.site.register(models.User, UserAdmin)
