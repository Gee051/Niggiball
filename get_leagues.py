import requests
from decouple import config
from datetime import datetime, timedelta

api_key = config('API_FOOTBALL_KEY')
base_url = 'https://v3.football.api-sports.io/'

headers = {
    'x-apisports-key': api_key
}

# Updated list of non-European countries
non_european_countries = [
    'Venezuela', 'Bhutan', 'Chile', 'Czechia', 'Denmark', 'Wales', 'Austria', 'Portugal','Argentina', 'China' ,
    'Belgium', 'Uruguay', 'Turkey', 'Sweden', 'Serbia', 'Romania', 'Qatar', 'Peru', 'Columbia',
    'Poland', 'Panama', 'Mexico', 'Japan', 'Malaysia', 'Greece', 'Azerbaijan', 'Georgia' , 'Kazakhstan',  'Cyprus', 'Armenia', 'Israel', 'Slovekia', 'Slovenia'
]

def fetch_upcoming_matches(days_ahead=7, limit=30):
    today = datetime.now()
    matches = []
    
    for i in range(days_ahead):
        current_day = today + timedelta(days=i)
        current_day_str = current_day.strftime('%Y-%m-%d')

        for country in non_european_countries:
            response = requests.get(f'{base_url}fixtures?date={current_day_str}', headers=headers)
            if response.status_code == 200:
                fixtures = response.json()['response']
                # Filter by the country
                country_matches = [fixture for fixture in fixtures if fixture['league']['country'] == country]
                matches.extend(country_matches[:limit])  # Add up to the limit for this country

                if len(matches) >= limit:
                    break  
        
        if len(matches) >= limit:
            break  
    
    return matches[:limit]  


matches = fetch_upcoming_matches()
for match in matches:
    print(f"{match['teams']['home']['name']} vs {match['teams']['away']['name']} on {match['fixture']['date']}")
