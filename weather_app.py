import requests


def get_weather(city: str):
    # Free weather API returning JSON data (no API key required)
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Extract current weather details from JSON
        current = data["current_condition"][0]
        area = data["nearest_area"][0]["areaName"][0]["value"]
        country = data["nearest_area"][0]["country"][0]["value"]

        temp_c = current["temp_C"]
        feels_like_c = current["FeelsLikeC"]
        humidity = current["humidity"]
        condition = current["weatherDesc"][0]["value"]
        wind_kmph = current["windspeedKmph"]

        # Display formatted output
        print(f"\n=== Weather Report for {area}, {country} ===")
        print(f"Condition   : {condition}")
        print(f"Temperature : {temp_c}°C (Feels like {feels_like_c}°C)")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_kmph} km/h")
        print("=" * 42)

    except requests.exceptions.HTTPError:
        print(f"Error: Could not find weather data for '{city}'. Please check the city name.")
    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
    except (KeyError, IndexError):
        print("Error: Unexpected data format received from the weather service.")


def main():
    print("--- Python CLI Weather App ---")
    city = input("Enter city name (e.g., Delhi, Mumbai, London): ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
