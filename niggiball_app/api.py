import requests
from decouple import config
from datetime import datetime, timedelta

api_key = config('API_FOOTBALL_KEY')
base_url = 'https://v3.football.api-sports.io/'

headers = {
    'x-apisports-key': api_key
}

def fetch_last_five_matches(team_id):
    """Fetch the last 5 matches for a given team."""
    response = requests.get(f'{base_url}fixtures?team={team_id}&last=5', headers=headers)
    if response.status_code == 200:
        return response.json()['response']
    return []

def fetch_upcoming_matches(days_ahead=7, limit=30):
    # Start fetching matches from the next day (tomorrow)
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    matches = []
    
    for i in range(days_ahead):
        # Start from tomorrow
        current_day = tomorrow + timedelta(days=i)
        current_day_str = current_day.strftime('%Y-%m-%d')

        # Fetch fixtures for the current day
        response = requests.get(f'{base_url}fixtures?date={current_day_str}', headers=headers)
        
        if response.status_code == 200:
            fixtures_data = response.json()
            
            if 'response' in fixtures_data:
                fixtures = fixtures_data['response']
                print(f"Fetched {len(fixtures)} matches for date {current_day_str}")

                # Add up to the limit of matches for this day
                matches.extend(fixtures[:limit - len(matches)])

                # Stop if we've already got the number of matches we need
                if len(matches) >= limit:
                    break
            else:
                print(f"No 'response' key found in API data for {current_day_str}")
        else:
            print(f"Failed to fetch matches for {current_day_str}, Status Code: {response.status_code}")
    
    return matches[:limit]  # Ensure only the specified limit of matches are returned


def predict_for_upcoming_matches(matches, limit=25):
    from .predictions import predict_outcome
    
    predictions = []

    for match in matches[:limit]:
 
        home_last_five = fetch_last_five_matches(match['teams']['home']['id'])
        away_last_five = fetch_last_five_matches(match['teams']['away']['id'])
        
        # Predict the outcome
        outcome = predict_outcome(home_last_five, away_last_five)
        
        # Store the prediction result
        predictions.append({
            'home_team': match['teams']['home']['name'],
            'away_team': match['teams']['away']['name'],
            'date': match['fixture']['date'],
            'predicted_outcome': outcome
        })
    
    return predictions

# Call this function to fetch upcoming matches and make predictions
upcoming_matches = fetch_upcoming_matches()

# Now make predictions for those matches
predictions = predict_for_upcoming_matches(upcoming_matches)

# Output the predictions
for prediction in predictions:
    print(f"{prediction['home_team']} vs {prediction['away_team']} on {prediction['date']} - Predicted Outcome: {prediction['predicted_outcome']}")


