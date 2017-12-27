from rest_framework import serializers

from ..models import Client, Doctor, Invitation


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'fullname', 'referral_code', 'username')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'fullname', 'email')


class InvitationSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    client = ClientSerializer()

    class Meta:
        model = Invitation
        fields = ('id', 'doctor', 'client', 'created', 'updated', 'status', 'is_sent')
