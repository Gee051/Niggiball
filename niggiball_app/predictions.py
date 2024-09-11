
def calculate_odd_even(matches):
    odd_count = 0
    even_count = 0
    
    for match in matches:
        if match['goals']['home'] is not None and match['goals']['away'] is not None:
            total_goals = match['goals']['home'] + match['goals']['away']
        else:
            continue
        
        if total_goals % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return 'odd' if odd_count > even_count else 'even'


def predict_outcome(home_last_five, away_last_five):
    home_outcome = calculate_odd_even(home_last_five)
    away_outcome = calculate_odd_even(away_last_five)

    if home_outcome == 'even' and away_outcome == 'even':
        return 'even'
    elif home_outcome == 'odd' and away_outcome == 'odd':
        return 'even'
    else:
        return 'odd'
