from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "create_at"]

admin.site.register(Player)