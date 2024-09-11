from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    attack_strength = models.FloatField(default=0.0)
    defense_strength = models.FloatField(default=0.0)
    recent_form = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)
    league = models.CharField(max_length=100)
    predicted_outcome = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"
