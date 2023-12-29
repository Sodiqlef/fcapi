from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

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
    query = request.GET.get('query')
    if query == None:
            clubs = Club.objects.all()
    else:
        clubs = Club.objects.filter(Q(name__icontains = query))
        
    if request.method == "GET":        
        clubs_serializer = ClubSerializer(clubs, many=True)
        data = clubs_serializer.data
        return Response(data)
    
    if request.method == "POST":
        club = Club.objects.create(
            name = request.data['name'],
            number_of_players = request.data['number_of_players'],
            position = request.data['position'],
            league = League.objects.get(name= request.data['league'])
        )
        clubs_serializer = ClubSerializer(clubs, many=True)
        data = clubs_serializer.data
        return Response(data)
    

@api_view(['GET', 'PUT', "DELETE"])
def club(request, name):
    try:
        club = Club.objects.get(name=name)
        if request.method == "GET":
            club_serializer = ClubSerializer(club, many=False)
            data = club_serializer.data
        if request.method == "PUT":
            club.name = request.data['name'],
            club.number_of_players = request.data['number_of_players'] ,
            club.position = int(request.data['position'])
            club.save()
            club_serializer = ClubSerializer(club, many=False)
            data = club_serializer.data
        if request.method == "DELETE":
            club.delete()
            club_serializer = ClubSerializer(club, many=False)
            data = club_serializer.data
    except ObjectDoesNotExist:
        data = {    'Return real object'}
    return Response(data)