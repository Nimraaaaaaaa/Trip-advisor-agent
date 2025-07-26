import requests

# Static lat/lon for major Pakistani cities
city_coords = {
    "lahore": (31.5497, 74.3436),
    "islamabad": (33.6844, 73.0479),
    "karachi": (24.8607, 67.0011),
    "swat": (35.2180, 72.4258),
    "gilgit": (35.9221, 74.3087),
    "quetta": (30.1798, 66.9750),
    "murree": (33.9062, 73.3916)
}

def get_weather_and_safety(city):
    city_key = city.lower()
    if city_key not in city_coords:
        return f"❌ City '{city}' not supported."
    lat, lon = city_coords[city_key]

    # Open-Meteo API for current weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        weather_resp = requests.get(weather_url, timeout=10)
        weather_data = weather_resp.json()
        current_weather = weather_data.get("current_weather", {})
    except Exception as e:
        return f"Weather API error: {e}"

    # REST Countries API for Pakistan
    country_url = "https://restcountries.com/v3.1/name/pakistan"
    try:
        country_resp = requests.get(country_url, timeout=10)
        country_data = country_resp.json()
        # Example: get region, population, etc. (not direct safety tips)
        region = country_data[0].get("region", "N/A")
        population = country_data[0].get("population", "N/A")
    except Exception as e:
        region = "N/A"
        population = "N/A"

    # Basic safety tip (static, can be improved)
    safety_tip = "Exercise usual safety precautions. Respect local customs and avoid isolated areas at night."

    return {
        "City": city.title(),
        "Temperature (C)": current_weather.get("temperature", "N/A"),
        "Weather": current_weather.get("weathercode", "N/A"),
        "Wind Speed (km/h)": current_weather.get("windspeed", "N/A"),
        "Region": region,
        "Population": population,
        "Safety Tip": safety_tip
    }

if __name__ == "__main__":
    city = input("Enter a Pakistani city (e.g., Lahore, Islamabad, Karachi): ")
    result = get_weather_and_safety(city)
    if isinstance(result, dict):
        print(f"\nWeather & Safety for {result['City']}:")
        print(f"Temperature: {result['Temperature (C)']}°C")
        print(f"Wind Speed: {result['Wind Speed (km/h)']} km/h")
        print(f"Region: {result['Region']}")
        print(f"Population: {result['Population']}")
        print(f"Safety Tip: {result['Safety Tip']}")
    else:
        print(result) 