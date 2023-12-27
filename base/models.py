from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    number_of_teams = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Club(models.Model):
    name = models.CharField(max_length=255)
    number_of_players = models.IntegerField()
    position = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='league')

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club')
    number_of_goals_scored = models.IntegerField()
    number_of_goals_assisted = models.IntegerField()
    

    def __str__(self) -> str:
        return self.name