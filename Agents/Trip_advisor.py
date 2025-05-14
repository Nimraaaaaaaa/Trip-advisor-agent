from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

Gemini_api_key =  os.environ.get("GEMINI_API_KEY")

print("Gemini api is set into enviroment.")
model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature=0.7,
    api_key=Gemini_api_key
)

response=model.invoke("Who is imran khan?").content
print(response)