import requests
import pandas as pd

def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "hourly": "temperature_2m",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame({
        "timestamp": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"]
    })

    return df
