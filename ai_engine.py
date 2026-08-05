import requests
import json
from prompts import RESUME_ANALYSIS_PROMPT

API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"

def get_analysis_from_ai(resume_text, api_key):

    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1500,
            "temperature": 0.2
        }
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        text = result[0]["generated_text"]

        text = text.replace(prompt, "").strip()
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {"error": str(e)}
        response.raise_for_status()

        text = response.json()["choices"][0]["message"]["content"]

        text = text.replace("```json","").replace("```","").strip()

        return json.loads(text)

    except Exception as e:

        return {
            "error": str(e)
        }
