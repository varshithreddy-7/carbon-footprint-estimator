from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me 1 tip to reduce carbon footprint"}]
)

print("✅ AI Suggestion:")
print(response.choices[0].message.content)
