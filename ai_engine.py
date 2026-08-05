import requests
import json
from prompts import RESUME_ANALYSIS_PROMPT

API_URL = "https://router.huggingface.co/v1/chat/completions"

def get_analysis_from_ai(resume_text, api_key):

    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        text = response.json()["choices"][0]["message"]["content"]

        text = text.replace("```json","").replace("```","").strip()

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e)
        }
