from django.contrib import admin
from .models import ElementCard, PureSubstanceCard, ToolCard, PureSubstanceElement


class ElementCardAdmin(admin.ModelAdmin):
    list_display = ["symbol", "number", "period", "family", "properties"]
    list_filter = ["period", "family"]
    search_fields = ["symbol", "number", "properties"]


class PureSubstanceElementInline(admin.TabularInline):
    model = PureSubstanceElement
    extra = 1


class PureSubstanceCardAdmin(admin.ModelAdmin):
    inlines = [PureSubstanceElementInline]
    list_display = ["name", "atomic_mass", "get_elements"]
    list_filter = ["elements"]

    def get_elements(self, obj):
        return ", ".join(
            [
                f"{ce.element.symbol}({ce.quantity})"
                for ce in obj.PureSubstance_elements.all()
            ]
        )

    get_elements.short_description = "構成元素"


admin.site.register(ElementCard, ElementCardAdmin)
admin.site.register(PureSubstanceCard, PureSubstanceCardAdmin)
admin.site.register(ToolCard)
