from re import search
from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    
    search_fields = ('email','firstname','lastname','start_date')
    ordering=('-start_date',)
    list_display = ('email','firstname','lastname','is_examiner','is_examinee')
    
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

admin.site.register(CustomUser,CustomUserAdmin)