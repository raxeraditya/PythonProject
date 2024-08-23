import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_APIKEY")
lat = os.getenv("LATTITUDE")
lon = os.getenv("LONGITUDE")
print(lat, lon, API_KEY)

CITY = "London"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
URL1 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"


def get_weather_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        dataframe = {
            "Temperature": [f"{temperature} K"],
            "Feels Like": [f"{feels_like} K"],
            "Humidity": [f"{humidity} %"],
            "Weather": [weather_description],
            "Wind Speed": [f"{wind_speed} m/s"],
            "Pressure": [f"{data['main']['pressure']} hPa"],
            "Visibility": [f"{data['visibility']} m"],
            "Cloudiness": [f"{data['clouds']['all']} %"],
            "Rain": [f"{data.get('rain', {}).get('1h', '0')} mm"],
            "Country": [data['sys']['country']]
        }

        # Convert the dictionary to a DataFrame
        df = pd.DataFrame(dataframe)
        excel_file_name = 'weather.xlsx'

        # Check if file exists to avoid overwriting
        if not os.path.isfile(excel_file_name):
            df.to_excel(excel_file_name, index=False)
        else:
            with pd.ExcelWriter(excel_file_name, mode='a', if_sheet_exists='overlay') as writer:
                # Get the last row in the existing Excel sheet
                reader = pd.read_excel(excel_file_name)
                df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

        return data
    except Exception as e:
        print(e)
    finally:
        print("good work")



def main():
    weather_data = get_weather_data(URL1)


if __name__ == "__main__":
    main()
