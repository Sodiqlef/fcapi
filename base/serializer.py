from rest_framework.serializers import ModelSerializer

from .models import Club, League, Player


class LeagueSerializer(ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class ClubSerializer(ModelSerializer):
    league = LeagueSerializer()
    class Meta:
        model = Club
        fields = ['name', 'number_of_players', 'position', 'league']