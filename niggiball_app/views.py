from django.shortcuts import render
from niggiball_app.api import fetch_upcoming_matches, fetch_last_five_matches
from .predictions import predict_outcome

def upcoming_predictions_view(request):
    matches = fetch_upcoming_matches()
    
    # Check if matches were fetched or if the API rate limit was hit
    if not matches:
        error_message = "No upcoming matches found or API rate limit exceeded. Please try again later."
        return render(request, 'predictions.html', {'predictions': [], 'error_message': error_message})

    predictions = []
    for match in matches:
        home_last_five = fetch_last_five_matches(match['teams']['home']['id'])
        away_last_five = fetch_last_five_matches(match['teams']['away']['id'])
        
        outcome = predict_outcome(home_last_five, away_last_five)
        
        # Add league, date, and time to predictions
        predictions.append({
            'home_team': match['teams']['home']['name'],
            'away_team': match['teams']['away']['name'],
            'date': match['fixture']['date'],
            'time': match['fixture']['timestamp'],
            'league': match['league']['name'],
            'predicted_outcome': outcome,
        })
    
    # Check if predictions are generated
    if not predictions:
        print("No predictions generated.")

    return render(request, 'predictions.html', {'predictions': predictions})
