from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
User = get_user_model()


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Permium, CustomUser




class CustomUserAdmin(BaseUserAdmin):

    model = User
    list_display = ('phone', 'is_staff', 'is_active','is_verified')
    list_filter = ('phone','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('password',),}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



class PermiumAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date_start', 'date_end','description',)
    list_filter = ('status',)
    search_fields = ('status',)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Permium, PermiumAdmin)




