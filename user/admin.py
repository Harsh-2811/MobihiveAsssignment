from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
User = get_user_model()

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Extra Details',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': ['profile_photo','address','city','phone_number','SecureCode']
,
            },
        ),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(QrCode)
