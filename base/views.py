from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Club, League, Player
from .serializer import ClubSerializer

# Create your views here.


@api_view(["GET"])
def endpoints(request):
    data = [
        'clubs/',
        'club/:name'
    ]
    return Response(data)


@api_view(["GET", "POST"])
def clubs(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query == None:
            clubs = Club.objects.all()
        else:
            clubs = Club.objects.filter(Q(name__icontains = query))
        clubs_serializer = ClubSerializer(clubs, many=True)
        data = clubs_serializer.data
        return Response(data)
    if request.method == "POST":
        clubs = Club.objects.create(
            name = request.data['name'],
            number_of_players = request.data['number_of_players'],
            position = request.data['position'],
            league = request.data['league']
        )
        clubs_serializer = ClubSerializer(clubs, many=True)
        data = clubs_serializer.data
        return Response(data)