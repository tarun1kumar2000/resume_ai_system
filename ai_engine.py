import requests
import json
from prompts import RESUME_ANALYSIS_PROMPT

API_URL = "https://openrouter.ai/api/v1/chat/completions"


def get_analysis_from_ai(resume_text, api_key):

    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.io",
        "X-Title": "AI Resume Screener"
    }

    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
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

        result = response.json()

        text = result["choices"][0]["message"]["content"]

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        return {
            "error": str(e)
        }        text = text.replace(prompt, "").strip()
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
