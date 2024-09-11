from django.core.management.base import BaseCommand
from niggiball_app.predictions import predict_outcome
from niggiball_app.models import Match

class Command(BaseCommand):
    help = 'Run predictions for upcoming matches'

    def handle(self, *args, **kwargs):
        upcoming_matches = Match.objects.filter(home_score__isnull=True)
        for match in upcoming_matches:
            outcome = predict_outcome(match.home_team.id, match.away_team.id)
            match.predicted_outcome = outcome
            match.save()
        self.stdout.write(self.style.SUCCESS('Successfully ran predictions'))
