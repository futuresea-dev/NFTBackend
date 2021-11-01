from django.contrib import admin
from .models import Serie, Token


@admin.register(Serie)
class AdminToken(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', )
    list_filter = ('title', )

@admin.register(Token)
class AdminToken(admin.ModelAdmin):
    list_display = ('number', 'author', 'serie')
    list_filter = ('serie', 'author', 'date')