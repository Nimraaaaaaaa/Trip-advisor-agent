from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.groq import Groq

# Load environment variables (for GROQ_API_KEY)
load_dotenv()

from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

def generate_narrative(destination, itinerary, user_name="Traveler"):
    if isinstance(itinerary, list):
        itinerary_str = "\n".join([f"Day {i+1}: {item}" for i, item in enumerate(itinerary)])
    else:
        itinerary_str = str(itinerary)

    prompt = f"""
    **Experience Narrator Agent** – Immersive Travel Story

    You are a creative AI travel narrator. Your job is to take the following destination and itinerary, and write a vivid, immersive, second-person narrative as if the user ({user_name}) is experiencing the trip. Make it engaging, sensory, and full of local color. Use present tense. Add small cultural or emotional details.

    Destination: {destination}
    Itinerary:
    {itinerary_str}

    Write a story for the user’s journey, day by day, as if they are living it.
    """

    agent = Agent(
        model=Groq(id="llama3-70b-8192"),
        markdown=True,
        stream=False,  # 🔁 Set stream=False if you want entire result as return
        system_message=prompt
    )
    
    return agent.invoke({"input": ""})  # You can pass input if needed, or just blank



if __name__ == "__main__":
    # Example usage
    destination = input("Enter your destination: ")
    # For demo, a simple itinerary list. Replace with your real itinerary data.
    itinerary = [
        "Arrive and explore the old city bazaar.",
        "Visit the grand mosque and try local street food.",
        "Take a day trip to the mountains and enjoy scenic views."
    ]
    print("\n🧳 Generating your immersive travel story...\n")
    print(generate_narrative(destination, itinerary)) 