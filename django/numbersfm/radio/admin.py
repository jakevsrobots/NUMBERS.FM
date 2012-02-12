from django.contrib import admin
from models import Show, ShowArchive


class ShowArchiveInline(admin.TabularInline):
    model = ShowArchive

class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ShowArchiveInline,)

admin.site.register(Show, ShowAdmin)
