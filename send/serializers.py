from rest_framework import serializers
from .models import Client, Message, Distribution

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'



class DistributionResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distribution
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("__all__")