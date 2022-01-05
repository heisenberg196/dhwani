from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from dhw.serializers import ChildSerializer, DistrictSerializer, StateSerializer
from .models import State, District, Child

class StateSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    serializer_class = StateSerializer
    queryset = State.objects.all()

class DistrictSet(viewsets.ModelViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class ChildSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser]
    permission_classes = [IsAuthenticated]
    serializer_class = ChildSerializer
    queryset = Child.objects.all()
