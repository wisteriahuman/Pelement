from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Element
from .serializers import ElementSerializer


class ElementView(APIView):
    def get(self, request):
        elements = Element.objects.all()
        serializer = ElementSerializer(elements, many=True)
        return Response(serializer.data)
    

class ElementDetailView(APIView):
    def get(self, request, number):
        element = Element.objects.get(number=number)
        serializer = ElementSerializer(element)
        return Response(serializer.data)