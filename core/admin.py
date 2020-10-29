from django.contrib import admin
from core.models import Article, Profile

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title", "views", "publicated", 
        "author", "created_dated", "updated_date"
        ]

    list_display_links = ["title", "author"]
    list_editable = ["publicated"]
    ordering = ["-views"]

    fields = ["title", "text", "created_dated", "udated_date"]
    readonly_fields = ["created_dated", "updated_date"]

    list_filter = ("publicated", "author", "created_dated")
    # list_per = 2
    
    search_fields = [
        "text", "title", "author__username", 
        "author__first_name", "author_last_name"
        ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile)