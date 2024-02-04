from django.contrib import admin
from .models import MenuItem



@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'parent', 'created_at', 'updated_at')
    list_filter = ('parent',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'named_url', 'url', 'parent'),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')




