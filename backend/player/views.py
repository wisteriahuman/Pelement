from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Player
from .serializers import PlayerSerializer


class PlayerView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        name = request.data.get("name")
        tool_deck = request.data.get("tool_deck", [])
        player = Player(name=name, tool_deck=tool_deck)
        player.save()
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

class PlayerDetailView(APIView):
    def get(self, request, id):
        player = Player.objects.get(id=id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    
    def put(self, request, id):
        player = Player.objects.get(id=id)
        player.name = request.data.get("name", player.name)
        player.tool_deck = request.data.get("tool_deck", player.tool_deck)
        player.save()
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    
    def delete(self, request, id):
        player = Player.objects.get(id=id)
        player.delete()
        return Response(status=204)