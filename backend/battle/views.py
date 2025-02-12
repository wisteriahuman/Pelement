from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count
from .models import Battle, BattleParticipant
from .serializers import BattleSerializer, BattleParticipantSerializer


class BattleView(APIView):
    def get(self, request):
        battles = Battle.objects.all()
        serializer = BattleSerializer(battles, many=True)
        return Response(serializer.data)

    def post(self, request):
        battle = Battle()
        battle.save()
        serializer = BattleSerializer(battle)
        return Response(serializer.data)

class BattleDetailView(APIView):
    def get(self, request, id):
        battle = Battle.objects.get(id=id)
        serializer = BattleSerializer(battle)
        return Response(serializer.data)

    def put(self, request, id):
        battle = Battle.objects.get(id=id)
        battle.state = request.data.get("state", battle.state)
        battle.winner = request.data.get("winner", battle.winner)
        battle.turn = request.data.get("turn", battle.turn)
        battle.pure_substance_deck = request.data.get("pure_substance_deck", battle.pure_substance_deck)
        battle.save()
        serializer = BattleSerializer(battle)
        return Response(serializer.data)

    def delete(self, request, id):
        battle = Battle.objects.get(id=id)
        battle.delete()
        return Response(status=204)


class BattleParticipantView(APIView):
    def get(self, request):
        participants = BattleParticipant.objects.all()
        serializer = BattleParticipantSerializer(participants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        battle_id = request.data.get("battle_id")
        player_id = request.data.get("player_id")
        role = request.data.get("role")
        life = request.data.get("life", 100)
        energy = request.data.get("energy", 40)
        nature_hand = request.data.get("nature_hand", [])
        tool_hand = request.data.get("tool_hand", [])
        tool_deck_copy = request.data.get("tool_deck_copy", [])
        participant = BattleParticipant(
            battle_id=battle_id,
            player_id=player_id,
            role=role,
            life=life,
            energy=energy,
            nature_hand=nature_hand,
            tool_hand=tool_hand,
            tool_deck_copy=tool_deck_copy
        )
        participant.save()
        serializer = BattleParticipantSerializer(participant)
        return Response(serializer.data)


class BattleParticipantDetailView(APIView):
    def get(self, request, id):
        participant = BattleParticipant.objects.get(battle=id)
        serializer = BattleParticipantSerializer(participant)
        return Response(serializer.data)
    
    def put(self, request, id):
        participant = BattleParticipant.objects.get(battle=id)
        participant.life = request.data.get("life", participant.life)
        participant.energy = request.data.get("energy", participant.energy)
        participant.nature_hand = request.data.get("nature_hand", participant.nature_hand)
        participant.tool_hand = request.data.get("tool_hand", participant.tool_hand)
        participant.tool_deck_copy = request.data.get("tool_deck_copy", participant.tool_deck_copy)
        participant.save()
        serializer = BattleParticipantSerializer(participant)
        return Response(serializer.data)
    
    def delete(self, request, id):
        participant = BattleParticipant.objects.get(battle=id)
        participant.delete()
        return Response(status=204)
    

class MatchmakingView(APIView):
    def post(self, request):
        player_id = request.data.get("player_id")
        if not player_id:
            return Response({"error": "player_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        waiting_battle_qs = Battle.objects.filter(state="preparation").annotate(num_participants=Count('participants')).filter(num_participants=1)
        if waiting_battle_qs.exists():
            waiting_battle = waiting_battle_qs.first()
            existing_participant = waiting_battle.participants.first()
            role = "player2" if existing_participant.role == "player1" else "player1"
            participant = BattleParticipant(
                battle=waiting_battle,
                player_id=player_id,
                role=role,
                life=100,
                energy=40,
                nature_hand=[],
                tool_hand=[],
                tool_deck_copy=[]
            )
            participant.save()
            battle = waiting_battle
        else:
            battle = Battle.objects.create()
            participant = BattleParticipant.objects.create(
                battle=battle,
                player_id=player_id,
                role="player1",
                life=100,
                energy=40,
                nature_hand=[],
                tool_hand=[],
                tool_deck_copy=[]
            )
        
        serializer = BattleSerializer(battle)
        return Response(serializer.data, status=status.HTTP_200_OK)