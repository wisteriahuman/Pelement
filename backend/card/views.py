from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ElementCard, CompoundCard, ToolCard
from .serializers import ElementCardSerializer, CompoundCardSerializer, ToolCardSerializer


class AllCardView(APIView):
    def get(self, request):
        element_cards = ElementCard.objects.all()
        compound_cards = CompoundCard.objects.all()
        tool_cards = ToolCard.objects.all()
        element_serializer = ElementCardSerializer(element_cards, many=True)
        compound_cards = CompoundCardSerializer(compound_cards, many=True)
        tool_cards = ToolCardSerializer(tool_cards, many=True)
        return Response({
            'element_cards': element_serializer.data,
            'compound_cards': compound_cards.data,
            'tool_cards': tool_cards.data,
        })


class ElementCardView(APIView):
    def get(self, request):
        element_cards = ElementCard.objects.all()
        serializer = ElementCardSerializer(element_cards, many=True)
        return Response(serializer.data)


class CompoundCardView(APIView):
    def get(self, request):
        compound_cards = CompoundCard.objects.all()
        serializer = CompoundCardSerializer(compound_cards, many=True)
        return Response(serializer.data)


class ToolCardView(APIView):
    def get(self, request):
        tool_cards = ToolCard.objects.all()
        serializer = ToolCardSerializer(tool_cards, many=True)
        return Response(serializer.data)