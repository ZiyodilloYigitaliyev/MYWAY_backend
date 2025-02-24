from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import (
    ServiceAddres, TexServiceOrder, Gas, CarOil, TexServiceMessage,

)
from .serializers import (
    ServiceAddresSerializer, TexServiceOrderSerializer, GasSerializer,
    CarOilSerializer,  TexServiceMessageSerializer,

)

# ServiceAddres API View
class ServiceAddresView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        addresses = ServiceAddres.objects.filter(user=request.user)
        serializer = ServiceAddresSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceAddresSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TexServiceOrder API View
class TexServiceOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = TexServiceOrder.objects.filter(user=request.user)
        serializer = TexServiceOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TexServiceOrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Gas API View
class GasView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        gas_records = Gas.objects.filter(user=request.user)
        serializer = GasSerializer(gas_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GasSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CarOil API View
class CarOilView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        car_oil_records = CarOil.objects.filter(user=request.user)
        serializer = CarOilSerializer(car_oil_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarOilSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# TexServiceMessage API View
class TexServiceMessageView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        messages = TexServiceMessage.objects.filter(user=request.user)
        serializer = TexServiceMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TexServiceMessageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




