from dotenv import load_dotenv
import os
import wikipedia

# Load environment variables (optional)
load_dotenv()

def get_cultural_guide(destination):
    try:
        search_term = f"Culture of {destination}"
        summary = wikipedia.summary(search_term, sentences=10)
        return f"**Cultural Summary for {destination}:**\n\n{summary}"
    except wikipedia.exceptions.PageError:
        return f"Sorry, no cultural page found for **{destination}**."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for **{destination}**: {e.options[:5]}"
    except Exception as e:
        return f"An error occurred: {e}"

# CLI testing (optional)
if __name__ == "__main__":
    dest = input("Enter destination: ")
    print(get_cultural_guide(dest))
