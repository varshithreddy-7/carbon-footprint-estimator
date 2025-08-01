from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def get_suggestions(travel, transport, diet, electricity, total):
    prompt = f"""
You are a sustainability expert. Suggest 3 practical and friendly tips to reduce carbon footprint based on:
- Transport mode: {transport}
- Weekly travel distance: {travel} km
- Diet: {diet}
- Electricity usage: {electricity} kWh/month
- Total carbon footprint: {total} kg CO₂/year

Present tips in numbered bullet points.
"""

    try:
        res = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = res.choices[0].message.content.strip()
        tips = [tip.strip("•1234567890.- ") for tip in content.split("\n") if tip.strip()]
        return tips
    except Exception as e:
        import traceback
        print("❌ Error while fetching suggestions from OpenRouter API:")
        print("Exception:", e)
        traceback.print_exc()
        return ["⚠️ Unable to fetch AI suggestions at the moment. Please try again later."]
