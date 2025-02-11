from django.contrib import admin
from .models import Element

class ElementAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'number', 'period', 'family', 'properties']
    list_filter = ['period', 'family']
    search_fields = ['symbol', 'number', 'properties']

admin.site.register(Element, ElementAdmin)