from django.contrib import admin
from models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'schedule_type')
    list_editable = ('is_active',)

admin.site.register(Show, ShowAdmin)
