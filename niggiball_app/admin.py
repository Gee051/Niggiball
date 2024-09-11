

from django.contrib import admin
from .models import Team, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'attack_strength', 'defense_strength', 'recent_form']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'date', 'home_score', 'away_score', 'league']
