from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ElementCard, PureSubstanceCard, ToolCard
from .serializers import (
    ElementCardSerializer,
    PureSubstanceCardSerializer,
    ToolCardSerializer,
)


class AllCardView(APIView):
    def get(self, request):
        element_cards = ElementCard.objects.all()
        PureSubstance_cards = PureSubstanceCard.objects.all()
        tool_cards = ToolCard.objects.all()
        element_serializer = ElementCardSerializer(element_cards, many=True)
        PureSubstance_cards = PureSubstanceCardSerializer(
            PureSubstance_cards, many=True
        )
        tool_cards = ToolCardSerializer(tool_cards, many=True)
        return Response(
            {
                "element_cards": element_serializer.data,
                "PureSubstance_cards": PureSubstance_cards.data,
                "tool_cards": tool_cards.data,
            }
        )


class ElementCardView(APIView):
    def get(self, request):
        element_cards = ElementCard.objects.all()
        serializer = ElementCardSerializer(element_cards, many=True)
        return Response(serializer.data)


class PureSubstanceCardView(APIView):
    def get(self, request):
        PureSubstance_cards = PureSubstanceCard.objects.all()
        serializer = PureSubstanceCardSerializer(PureSubstance_cards, many=True)
        return Response(serializer.data)


class ToolCardView(APIView):
    def get(self, request):
        tool_cards = ToolCard.objects.all()
        serializer = ToolCardSerializer(tool_cards, many=True)
        return Response(serializer.data)
