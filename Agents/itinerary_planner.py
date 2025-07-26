import requests
from bs4 import BeautifulSoup

def get_wikivoyage_section_text(city, section_title="Itinerary"):
    url = "https://en.wikivoyage.org/w/api.php"
    # First, get the section index for the desired section
    params = {
        "action": "parse",
        "page": city,
        "format": "json",
        "prop": "sections"
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    section_index = None
    for section in data.get("parse", {}).get("sections", []):
        if section_title.lower() in section["line"].lower():
            section_index = section["index"]
            break
    if not section_index:
        return None

    # Now, get the text of that section
    params = {
        "action": "parse",
        "page": city,
        "format": "json",
        "prop": "text",
        "section": section_index
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    html = data.get("parse", {}).get("text", {}).get("*", "")
    soup = BeautifulSoup(html, "html.parser")
    # Extract plain text from HTML
    text = soup.get_text(separator="\n")
    return text.strip()

def plan_itinerary(city, days=3):
    # Try to get 'Itinerary' section, else fallback to 'See'
    itinerary = get_wikivoyage_section_text(city, "Itinerary")
    if not itinerary:
        itinerary = get_wikivoyage_section_text(city, "See")
    if not itinerary:
        return f"No itinerary or main attractions found for {city} on Wikivoyage."
    return itinerary

if __name__ == "__main__":
    city = input("Enter your destination city: ")
    days = int(input("How many days is your trip? (for future use): "))
    print("\n🗺️ Wikivoyage-based itinerary:\n")
    plan = plan_itinerary(city, days)
    print(plan) 