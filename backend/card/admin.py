from django.contrib import admin
from .models import ElementCard, CompoundCard, ToolCard


admin.site.register([ElementCard, CompoundCard, ToolCard])