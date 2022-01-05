from rest_framework import serializers
from dhw.models import State, District, Child

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('__all__')

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('__all__')

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('__all__')