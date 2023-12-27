from rest_framework.serializers import ModelSerializer

from .models import Club, League, Player


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'