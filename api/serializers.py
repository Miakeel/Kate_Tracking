from rest_framework import serializers
from Tracking.models import Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        # fields = ['first_name', 'last_name','institution','email','title']
        fields = '__all__'