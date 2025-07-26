

 Trip Advisor Agent

An intelligent travel assistant powered by Large Language Models (LLMs) to help users generate personalized travel recommendations, hotel suggestions, and multi-day itineraries.

---

 🌍 Overview

The Trip Advisor Agent is designed to assist users in planning their trips by leveraging:
- Language models (like OpenAI's GPT) for future use
- Custom agent workflows (Agno workflows)
- Optional integration with search tools (like Serper, Google Search)

It helps users by:
- Suggesting destinations
- Recommending hotels, restaurants, and local attractions
- Creating full travel itineraries

---

## 🚀 Features

- 🧠 Smart trip planning using LLMs
- 📍 Location-based recommendations
- 🏨 Hotel, food, and activity suggestions
- 📅 Day-by-day itinerary generation
- 🔎 Optional integration with external search tools

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Nimraaaaaaaa/Trip-advisor-agent.git
cd Trip-advisor-agent
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up your `.env` file with API keys (if needed):**

```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key (optional)
```

---

## 🧪 Usage

You can run the app as a script or through a user interface (if added):

```bash
python main.py
```

Or with Streamlit (if integrated):

```bash
streamlit run app.py
```

The system will ask for user inputs like destination, number of days, and preferences — then generate a customized itinerary and recommendations.

---

## 📁 Suggested Project Structure

```
Trip-advisor-agent/
├── main.py
├── agents/
│   ├── itinerary_agent.py
│   ├── hotel_agent.py
│   └── search_agent.py
├── tools/
│   ├── search_tool.py
│   └── prompt_templates.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. User provides destination, number of days, and travel preferences.
2. Agent generates prompts to search for relevant information.
3. Optionally fetches data using search tools or APIs.
4. LLM builds a full itinerary or answers the user query.

---

## 🔐 Environment Variables

| Variable         | Description                     |
| ---------------- | ------------------------------- |
| `OPENAI_API_KEY` | Required to access GPT model    |
| `SERPER_API_KEY` | Optional for search integration |

---

## 📝 Example Input

* Destination: **Tokyo**
* Days: **5**
* Theme: **Food lover**

The agent will return:

* 5-day Tokyo itinerary
* Restaurant suggestions
* Hotel options

---

## 👥 Contributing

Contributions are welcome!

```bash
git checkout -b feature/your-feature
git commit -m "Add new feature"
git push origin feature/your-feature
```

Then open a Pull Request 🚀

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [OpenAI](https://openai.com/) for GPT APIs
* [Serper.dev](https://serper.dev/) for optional web search integration
* Community resources and tools

---

⭐ If you find this project useful, consider giving it a **star** on GitHub!

```

---

Let me know if you want a `requirements.txt` file or badges (like Python version, license, stars) at the top as well.
```

