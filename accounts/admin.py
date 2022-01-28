from re import search
from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# setting representation of data for CustomUser model in django admin.
class CustomUserAdmin(admin.ModelAdmin):
    # choosig model
    model = CustomUser
    # setting up search fields
    search_fields = ('email','firstname','lastname','start_date')
    # setting up ordering 
    ordering=('-start_date',)
    # setting list to be displayed on saving data in db.
    list_display = ('email','firstname','lastname','is_examiner','is_examinee')
    
    # Required Field to be in User Database in django (all will be below format)
    fieldsets = (
        (None, {"fields": (
               'email','username','firstname','lastname', 'password',
            ),
        }),
        ('Permissions', {"fields": (
               'is_active','is_staff','is_superuser',
            ),
        }),
        ('Profile Category', {"fields": (
               'is_examiner','is_examinee',
            ),
        }),
        ('Personal', {"fields": (
               'about',
            ),
        }),
    )

# Register CustomUser model in CustomUserAdmin format.
admin.site.register(CustomUser,CustomUserAdmin)