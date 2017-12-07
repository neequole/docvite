from rest_framework import serializers

from ..models import Client, Doctor, Invitation


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'referral_code', 'username')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email')


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('doctor', 'client', 'created', 'updated', 'status', 'is_sent')
