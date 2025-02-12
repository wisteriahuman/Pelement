from rest_framework import serializers
from .models import ElementCard, CompoundCard, ToolCard

class ElementCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementCard
        fields = '__all__'
        
class CompoundCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompoundCard
        fields = '__all__'

class ToolCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolCard
        fields = '__all__'