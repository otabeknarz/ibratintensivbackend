from rest_framework import serializers
from .models import People, TGPeople


class TGPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGPeople
        fields = 'id', 'name'


class TGPeopleSerializerM2M(serializers.ModelSerializer):
    invited_friends = TGPeopleSerializer(many=True)

    class Meta:
        model = TGPeople
        fields = 'id', 'name', 'invited_friends'


class TGPeopleIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGPeople
        fields = "id",
