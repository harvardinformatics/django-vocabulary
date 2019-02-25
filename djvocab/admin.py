"""
Django admin for vocabulary table
"""

from django.contrib import admin
from djvocab.models import Vocabulary

class VocabularyAdmin(admin.ModelAdmin):
    fields = ('key', 'value', 'description', 'order')
    list_display = ('key', 'value', 'description', 'order')
    ordering = ('key', )
    search_fields = ('key','value')

admin.site.register(Vocabulary, VocabularyAdmin)

