from rest_framework import serializers
from .models import Battle, BattleParticipant


class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = "__all__"


class BattleParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleParticipant
        fields = "__all__"