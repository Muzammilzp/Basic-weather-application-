import requests

def get_weather(location):
    url = f"https://wttr.in/{location}?format=j1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def display_weather(data, location):
    try:
        current = data["current_condition"][0]
        
        temperature = current["temp_C"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]

        print("\n=== Current Weather ===")
        print(f"Location: {location}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
        print(f"Wind Speed: {wind_speed} km/h")

    except (KeyError, IndexError):
        print("Error parsing weather data.")

def main():
    print("=== Weather App (No API Key Required) ===")
    location = input("Enter city name or ZIP code: ").strip()

    if not location:
        print("Please enter a valid location.")
        return

    weather_data = get_weather(location)

    if weather_data:
        display_weather(weather_data, location)
    else:
        print("Could not retrieve weather data. Check your internet connection or location.")

if __name__ == "__main__":
    main()
