from openai import OpenAI
import json
from prompts import RESUME_ANALYSIS_PROMPT


def get_analysis_from_ai(resume_text, api_key):

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    prompt = RESUME_ANALYSIS_PROMPT.format(           
        resume_text=resume_text
    )

    try:

        response = client.chat.completions.create(
            "model": "openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        text = response.choices[0].message.content

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        return {
            "error": str(e)
        }
