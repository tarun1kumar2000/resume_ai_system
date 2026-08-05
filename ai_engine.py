import google.generativeai as genai
import json
from dotenv import load_dotenv
from prompts import RESUME_ANALYSIS_PROMPT

load_dotenv()

def get_analysis_from_ai(resume_text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)

    try:
        response = model.generate_content(prompt)

        json_text = (
            response.text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(json_text)

    except Exception as e:
        return {
            "error": f"AI Analysis failed: {str(e)}"
        }
