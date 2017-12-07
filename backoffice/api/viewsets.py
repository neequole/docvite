from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

from itsdangerous import BadSignature
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import ClientSerializer, DoctorSerializer, \
    InvitationSerializer
from ..models import Client, Doctor, Invitation
from ..permissions import DoctorOnly

# TODO: Need to review permission for basic endpoints


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
        doctor = Doctor.objects.filter(pk=user.pk).exists() if user else None
        if doctor:
            login(request, user)
            serializer = self.get_serializer(instance=user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            data = {'detail': AuthenticationFailed.default_detail}
            return Response(status=status.HTTP_401_UNAUTHORIZED, data=data)

    @list_route(methods=['post'], permission_classes=(DoctorOnly,))
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

    @detail_route(url_path='invitations')
    def get_invitations(self, request, pk):
        doctor = self.get_object()
        invitations = Invitation.objects.filter(doctor=doctor)
        serializer = InvitationSerializer(data=invitations, many=True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @list_route(methods=['post'], permission_classes=(DoctorOnly,))
    def invite(self, request):
        email = request.data.get('email')
        if not email:
            raise ValidationError({'email': 'Required'})
        # check if there is a client with this e-mail
        client = Client.objects.filter(email=email).first()
        if not client:
            raise ValidationError({'email': 'Client with this email not found.'})
        # TODO: need to confirm we can send out multiple pending invites
        # send out the invitation
        invitation = Invitation.send(request.user, client)
        serializer = InvitationSerializer(instance=invitation)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    @list_route(url_path='(?P<hash_pk>[^/.]+)/accept', permission_classes=(AllowAny,))
    def accept(self, request, hash_pk):
        # check if valid hash
        try:
            pk = Invitation.deserialize_id(hash_pk)
        except BadSignature as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # check if hash pertains to an invitation
        invitation = get_object_or_404(Invitation, pk=pk)
        invitation.accept()
        serializer = self.serializer_class(instance=invitation)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

