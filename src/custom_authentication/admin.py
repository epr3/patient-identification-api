from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, RefreshToken, PatientCard


class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'pnc', 'email', 'date_of_birth', 'first_name',
                    'last_name', 'is_superuser', 'is_medic', 'is_patient', )
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class PatientCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'insure_code', 'expiry_date', 'assigned_medic')


class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'expiry_date', 'user')

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(PatientCard, PatientCardAdmin)
admin.site.register(RefreshToken, RefreshTokenAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
