
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Message, Client, Distribution
from .serializers import DistributionResponseSerializer, ClientSerializer, MessageSerializer, UpdateClientSerializer

class ListCreateClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateClientSerializer
        return ClientSerializer


class RUDClientAPIView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class DistributionListCreateAPIView(viewsets.ModelViewSet):
    serializer_class = DistributionResponseSerializer
    queryset = Distribution.objects.all()

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        """
        Сводные данные по конкретной рассылке
        """
        queryset = Distribution.objects.all()
        mailing = get_object_or_404(queryset, pk=pk)
        serializer = DistributionResponseSerializer(mailing)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullinfo(self, request):
        """
        Сводные данные по всем рассылкам
        """
        queryset = Distribution.objects.all()
        serializer = DistributionResponseSerializer(queryset, many=True)
        return Response(serializer.data)


# class RUDClientAPIView(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     lookup_field = "pk"
#
#     def get_serializer_class(self):
#         if self.request.method == "PATCH":
#             return UpdateClientSerializer
#         return ClientSerializer