RESUME_ANALYSIS_PROMPT = """
You are an expert HR Manager and ATS (Applicant Tracking System) specialist.
Analyze the provided resume text and return a strictly structured JSON response.

Resume Text:
{resume_text}

The JSON output must follow this exact structure:
{{
  "candidate_info": {{
    "name": "",
    "email": "",
    "phone": "",
    "education": [{{ "degree": "", "branch": "", "university": "", "year": "" }}],
    "experience": [{{ "role": "", "company": "", "duration": "" }}]
  }},
  "technical_skills": {{
    "languages": [],
    "web_technologies": [],
    "frameworks": [],
    "databases": [],
    "cloud_devops": [],
    "ml_ai_data_science": [],
    "other_tools": []
  }},
  "soft_skills": [],
  "professional_summary": "",
  "job_recommendation": {{
    "role": "",
    "confidence_score": 0,
    "reason": ""
  }},
  "missing_skills": {{
    "high_priority": [],
    "medium_priority": [],
    "suggested_learning_path": ""
  }},
  "ats_analysis": {{
    "overall_score": 0,
    "keyword_match_percentage": 0,
    "keywords_found": [],
    "missing_keywords": [],
    "strengths": [],
    "weaknesses": [],
    "improvement_suggestions": []
  }}
}}

Instructions:
1. If information is missing, use "Not Found".
2. Confidence score and ATS score should be between 0 and 100.
3. Be objective and critical in ATS analysis.
4. Return ONLY the JSON object.
"""
