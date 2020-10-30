from datetime import date, timedelta
from pprint import pprint

import requests


def get_rate(currencies=["USD"], days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={symbols}"
    r = requests.get(requete)

    if not r and not r.json(): # pas besoin de verif 200 car si non ben false, AND verif si bien json
        return False, False #false devise et false jour

    api_rates = r.json().get("rates") # donc je recupere json et tout ce qui en clef rate

    all_rates = {currency: [] for currency in currencies} # comprehension de liste, non de tableau
    # on prend uniquement les jours et on verif l'ordre
    all_days = sorted(api_rates.keys())
    
    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]
        
    return all_days, all_rates

if __name__ == "__main__":
    days, rates = get_rate(currencies=["USD", "CAD"])
   
   
