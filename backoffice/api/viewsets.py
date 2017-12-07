from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import ClientSerializer, DoctorSerializer
from ..models import Client, Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @list_route(methods=['post'], permission_classes=(AllowAny,))
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # Check if doctor
        doctor = Doctor.objects.filter(pk=user.pk).first() if user else None
        if doctor:
            login(request, user)
            serializer = self.get_serializer(instance=user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            data = {'detail': AuthenticationFailed.default_detail}
            return Response(status=status.HTTP_401_UNAUTHORIZED, data=data)

    @list_route(methods=['post'])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
