from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Affidavit, RestoreLicense, Department
from .serializers import AffidavitSerializer, RestoreLicenseSerializer, DepartmentSerializer



# Affidavit API View
class AffidavitView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        affidavits = Affidavit.objects.filter(user=request.user)
        serializer = AffidavitSerializer(affidavits, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AffidavitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# RestoreLicense API View
class RestoreLicenseView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        licenses = RestoreLicense.objects.filter(user=request.user)
        serializer = RestoreLicenseSerializer(licenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestoreLicenseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Department API View
class DepartmentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        departments = Department.objects.filter(user=request.user)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

