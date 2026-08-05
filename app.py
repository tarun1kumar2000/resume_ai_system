import streamlit as st
from parser_utils import extract_text_from_pdf, extract_text_from_docx
from ai_engine import get_analysis_from_ai
from styles import apply_custom_css

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Resume Intelligence",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.markdown("## Resume Intelligence")
    st.caption("AI Resume Analysis Platform")

    st.divider()

    try:
        api_key = st.secrets["OPENROUTER_API_KEY"]
        st.success("API Connected")
    except Exception:
        api_key = st.text_input(
            "OpenRouter API Key",
            type="password",
            placeholder="sk-or-v1-xxxxxxxx"
        )

    st.divider()

    st.markdown("### Features")

    st.markdown("""
- Resume Parsing
- ATS Score
- Job Recommendation
- Skill Analysis
- Gap Analysis
- Professional Summary
""")

    st.divider()

    st.caption("Version 1.0")

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
"""
<div style="background:white;
padding:28px;
border-radius:16px;
border:1px solid #E5E7EB;
margin-bottom:25px;">

<h2 style="margin-bottom:8px;color:#111827;">
Resume Intelligence
</h2>

<p style="color:#6B7280;
font-size:16px;
margin-bottom:0;">
AI-powered resume analysis, ATS evaluation and career recommendations.
</p>

</div>
""",
unsafe_allow_html=True
)

# -------------------------------------------------
# Upload Section
# -------------------------------------------------

st.markdown("### Upload Resume")

uploaded_file = st.file_uploader(
    "",
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX"
)

st.caption(
    "Upload your latest resume to receive an ATS score, skill analysis, professional summary and job recommendation."
)

# -------------------------------------------------
# Processing
# -------------------------------------------------

if uploaded_file:

    if not api_key:

        st.warning("Please enter your OpenRouter API key.")

    else:

        with st.spinner("Analyzing your resume..."):

            file_extension = uploaded_file.name.split(".")[-1].lower()

            if file_extension == "pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)

            analysis = get_analysis_from_ai(
                resume_text,
                api_key
            )

            if "error" in analysis:

                st.error(analysis["error"])

            else:
                                # ==========================================
                # Dashboard Overview
                # ==========================================

                info = analysis.get("candidate_info", {})
                rec = analysis.get("job_recommendation", {})
                ats = analysis.get("ats_analysis", {})
                score = rec.get("confidence_score", 0)
                ats_score = ats.get("overall_score", 0)

                st.markdown("## Dashboard")

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.metric(
                        "ATS Score",
                        ats_score
                    )

                with c2:
                    st.metric(
                        "Recommended Role",
                        rec.get("role", "-")
                    )

                with c3:
                    st.metric(
                        "Match Confidence",
                        f"{score}%"
                    )

                st.divider()

                # ==========================================
                # Profile + Recommendation
                # ==========================================

                left, right = st.columns([1, 1])

                with left:

                    st.subheader("Candidate Profile")

                    st.write(
                        "**Name:**",
                        info.get("name", "-")
                    )

                    st.write(
                        "**Email:**",
                        info.get("email", "-")
                    )

                    education = info.get("education", [])

                    if education:

                        with st.expander("Education", expanded=True):

                            for edu in education:

                                st.markdown(
                                    f"""
**{edu.get('degree')}**

{edu.get('branch')}

{edu.get('year')}
"""
                                )

                    experience = info.get("experience", [])

                    if experience:

                        with st.expander("Experience"):

                            for exp in experience:

                                st.markdown(
                                    f"""
**{exp.get('role')}**

{exp.get('company')}

{exp.get('duration')}
"""
                                )

                with right:

                    st.subheader("Job Recommendation")

                    st.progress(score / 100)

                    st.write(
                        f"**Confidence:** {score}%"
                    )

                    st.info(
                        rec.get("reason", "")
                    )

                st.divider()

                # ==========================================
                # ATS + Summary
                # ==========================================

                left, right = st.columns([1, 2])

                with left:

                    st.subheader("ATS Analysis")

                    st.markdown(
                        f"""
<div class="ats-score-card">

<h1>{ats_score}</h1>

<p>Overall ATS Score</p>

</div>
""",
                        unsafe_allow_html=True
                    )

                    st.write(
                        "**Keyword Match:**",
                        f"{ats.get('keyword_match_percentage',0)}%"
                    )

                with right:

                    st.subheader("Professional Summary")

                    st.write(
                        analysis.get(
                            "professional_summary",
                            "-"
                        )
                    )

                st.divider()

                # ==========================================
                # Skills
                # ==========================================

                st.subheader("Skills")

                tech_col, soft_col = st.columns(2)

                with tech_col:

                    st.markdown("#### Technical Skills")

                    tech = analysis.get(
                        "technical_skills",
                        {}
                    )

                    for category, skills in tech.items():

                        if skills:

                            st.caption(
                                category.replace("_", " ").title()
                            )

                            html = "".join(
                                [
                                    f"<span class='skill-badge'>{skill}</span>"
                                    for skill in skills
                                ]
                            )

                            st.markdown(
                                html,
                                unsafe_allow_html=True
                            )

                with soft_col:

                    st.markdown("#### Soft Skills")

                    soft = analysis.get(
                        "soft_skills",
                        []
                    )

                    html = "".join(
                        [
                            f"<span class='skill-badge'>{skill}</span>"
                            for skill in soft
                        ]
                    )

                    st.markdown(
                        html,
                        unsafe_allow_html=True
                    )

                st.divider()
                                # ==========================================
                # Gap Analysis
                # ==========================================

                st.subheader("Gap Analysis")

                tab1, tab2, tab3 = st.tabs(
                    [
                        "Missing Skills",
                        "Strengths",
                        "Suggestions"
                    ]
                )

                # ------------------------
                # Missing Skills
                # ------------------------

                with tab1:

                    missing = analysis.get(
                        "missing_skills",
                        {}
                    )

                    high_priority = missing.get(
                        "high_priority",
                        []
                    )

                    if high_priority:

                        st.markdown(
                            "#### High Priority Skills"
                        )

                        html = "".join(
                            [
                                f"<span class='skill-badge'>{skill}</span>"
                                for skill in high_priority
                            ]
                        )

                        st.markdown(
                            html,
                            unsafe_allow_html=True
                        )

                    learning_path = missing.get(
                        "suggested_learning_path",
                        ""
                    )

                    if learning_path:

                        st.markdown("#### Learning Path")

                        st.info(
                            learning_path
                        )

                # ------------------------
                # Strengths
                # ------------------------

                with tab2:

                    strengths = ats.get(
                        "strengths",
                        []
                    )

                    if strengths:

                        for item in strengths:

                            st.success(item)

                    else:

                        st.write(
                            "No strengths identified."
                        )

                # ------------------------
                # Suggestions
                # ------------------------

                with tab3:

                    weaknesses = ats.get(
                        "weaknesses",
                        []
                    )

                    if weaknesses:

                        st.markdown(
                            "#### Areas to Improve"
                        )

                        for item in weaknesses:

                            st.error(item)

                    suggestions = ats.get(
                        "improvement_suggestions",
                        []
                    )

                    if suggestions:

                        st.markdown(
                            "#### Recommendations"
                        )

                        for tip in suggestions:

                            st.write(f"• {tip}")

                st.divider()

                st.caption(
                    "Analysis generated using AI. Results are intended to assist."
                )
