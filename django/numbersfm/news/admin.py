from django.contrib import admin
from models import NewsPost


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'date_published')
    list_filter_by = ('is_published',)
    list_editable = ('is_published',)
    filter_horizontal = ('related_shows',)


admin.site.register(NewsPost, NewsPostAdmin)
