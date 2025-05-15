from dotenv import load_dotenv
import os
from datetime import datetime
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

load_dotenv()

interest ="Islamabad pakistan"
budget = "5000rs"
travel_date= "may 2025"
agent = Agent(
    model=Groq(id="qwen-qwq-32b"),
    tools=[DuckDuckGoTools()],
    markdown=True,
    stream=True,
    system_message=f"""
    **Travel Scout Agent** - Direct Recommendations
    You're helping plan a trip to {interest} with:
    - Budget: {budget}
    - Travel Period: {travel_date}
    
    Provide 5-7 locations with:
    1. Cost estimates
    2. Best visiting times
    3. Key features
    4. Seasonal advice
    """
)

print(agent.print_response())