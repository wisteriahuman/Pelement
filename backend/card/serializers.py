from rest_framework import serializers
from .models import ElementCard, PureSubstanceCard, ToolCard


class ElementCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementCard
        fields = "__all__"


class PureSubstanceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PureSubstanceCard
        fields = "__all__"


class ToolCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolCard
        fields = "__all__"
