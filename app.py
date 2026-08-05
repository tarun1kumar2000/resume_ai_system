import streamlit as st
import os
from parser_utils import extract_text_from_pdf, extract_text_from_docx
from ai_engine import get_analysis_from_ai
from styles import apply_custom_css

# Page Config
st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="wide")
apply_custom_css()

# Sidebar
with st.sidebar:
    st.title("⚙️ Configuration")

    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        st.success("✅ Token Loaded")
    except Exception:
        api_key = st.text_input(
            "Enter OpenRouter API Key",
            type="password"
        )

    st.divider()
    st.markdown("### About")
    st.caption("AI-powered tool for Resume Analysis, Job Recommendation, and ATS Scoring.")
    
# Main Header
st.title("🚀 AI Resume Screening & Recommendation")
st.markdown("Upload a resume to get instant AI-driven career insights and ATS evaluation.")

# File Uploader
uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to proceed.")
    else:
        with st.spinner("🔄 Processing Resume..."):
            # 1. Extraction
            file_extension = uploaded_file.name.split(".")[-1].lower()
            if file_extension == "pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)

            # 2. AI Analysis
            analysis = get_analysis_from_ai(resume_text, api_key)

            if "error" in analysis:
                st.error(analysis["error"])
            else:
                # --- DASHBOARD LAYOUT ---
                
                # Top Row: Basic Info & Recommendation
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("👤 Candidate Profile")
                    info = analysis.get("candidate_info", {})
                    st.write(f"**Name:** {info.get('name')}")
                    st.write(f"**Email:** {info.get('email')}")
                    
                    with st.expander("🎓 Education"):
                        for edu in info.get("education", []):
                            st.write(f"• {edu.get('degree')} in {edu.get('branch')} ({edu.get('year')})")
                    
                    with st.expander("💼 Experience"):
                        for exp in info.get("experience", []):
                            st.write(f"• **{exp.get('role')}** at {exp.get('company')} ({exp.get('duration')})")

                with col2:
                    st.subheader("🎯 Job Recommendation")
                    rec = analysis.get("job_recommendation", {})
                    score = rec.get("confidence_score", 0)
                    
                    st.metric("Recommended Role", rec.get("role"))
                    st.progress(score / 100)
                    st.write(f"**Match Confidence:** {score}%")
                    st.info(rec.get("reason"))

                st.divider()

                # Second Row: ATS Score & Summary
                col3, col4 = st.columns([1, 2])
                
                with col3:
                    st.subheader("📊 ATS Analysis")
                    ats = analysis.get("ats_analysis", {})
                    ats_score = ats.get("overall_score", 0)
                    
                    color = "green" if ats_score > 70 else "orange" if ats_score > 40 else "red"
                    st.markdown(f"""
                        <div style="background-color:{color}; padding:20px; border-radius:10px; text-align:center; color:white;">
                            <h2 style="margin:0;">{ats_score}</h2>
                            <p style="margin:0;">Overall ATS Score</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.write(f"**Keyword Match:** {ats.get('keyword_match_percentage')}%")

                with col4:
                    st.subheader("📝 Professional Summary")
                    st.write(analysis.get("professional_summary"))

                st.divider()

                # Third Row: Skills
                st.subheader("🛠️ Skills Analysis")
                s_col1, s_col2 = st.columns(2)
                
                with s_col1:
                    st.markdown("**Technical Skills**")
                    tech_skills = analysis.get("technical_skills", {})
                    for category, skills in tech_skills.items():
                        if skills:
                            st.caption(category.replace("_", " ").title())
                            skill_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
                            st.markdown(skill_html, unsafe_allow_html=True)
                
                with s_col2:
                    st.markdown("**Soft Skills**")
                    soft_skills = analysis.get("soft_skills", [])
                    skill_html = "".join([f'<span class="skill-badge">{s}</span>' for s in soft_skills])
                    st.markdown(skill_html, unsafe_allow_html=True)

                st.divider()

                # Bottom Row: Improvements
                st.subheader("📈 Gap Analysis & Suggestions")
                tab1, tab2, tab3 = st.tabs(["Missing Skills", "Strengths", "Weaknesses & Tips"])
                
                with tab1:
                    missing = analysis.get("missing_skills", {})
                    st.warning("**High Priority Missing Skills:** " + ", ".join(missing.get("high_priority", [])))
                    st.info("**Learning Path:** " + missing.get("suggested_learning_path", ""))
                
                with tab2:
                    for s in ats.get("strengths", []):
                        st.success(f"✅ {s}")
                
                with tab3:
                    for w in ats.get("weaknesses", []):
                        st.error(f"❌ {w}")
                    st.markdown("**Improvement Tips:**")
                    for tip in ats.get("improvement_suggestions", []):
                        st.write(f"💡 {tip}")

                st.success("✅ Successfully Loaded")
