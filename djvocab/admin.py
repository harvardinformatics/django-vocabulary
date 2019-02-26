"""
Django admin for vocabulary table
"""

from django.contrib import admin
from djvocab.models import Vocabulary

class VocabularyAdmin(admin.ModelAdmin):
    fields = ('key', 'value', 'description', 'order')
    list_display = ('id', 'key', 'value', 'description', 'order')
    ordering = ('key', )
    search_fields = ('key','value')
    list_editable = ('key', 'value', 'description', 'order')

admin.site.register(Vocabulary, VocabularyAdmin)

