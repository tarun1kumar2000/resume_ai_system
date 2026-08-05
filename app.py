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
import streamlit as st
from parser_utils import extract_text_from_pdf, extract_text_from_docx
from ai_engine import get_analysis_from_ai
from styles import apply_custom_css
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Resume Intelligence",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("""
    <div style="margin-bottom:15px;">
        <h2 style="margin-bottom:0;">Resume Intelligence</h2>
        <p style="color:#6B7280;font-size:14px;">
            AI Resume Analysis Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("#### Features")

    st.markdown("""
- Resume Parsing
- ATS Evaluation
- Skill Analysis
- Job Recommendation
- Gap Analysis
- Professional Summary
""")

    st.divider()

    st.caption("Resume Intelligence v1.0")

# ==========================================================
# Hero Section
# ==========================================================

st.markdown("""
<div class="hero">

<h2 style="margin-bottom:8px;">
Resume Intelligence
</h2>

<p>
AI-powered resume analysis that evaluates ATS compatibility,
extracts skills, summarizes experience and recommends the
best-fit job role.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# Upload Section
# ==========================================================

upload_left, upload_right = st.columns([3,1])

with upload_left:

    st.markdown("### Upload Resume")

    uploaded_file = st.file_uploader(
        "",
        type=["pdf","docx"],
        help="Supported formats: PDF and DOCX"
    )

    st.caption(
        "Supported file types: PDF (.pdf) and Microsoft Word (.docx)"
    )

with upload_right:

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        """
**What you'll get**

• ATS Score

• Job Recommendation

• Skills Analysis

• AI Summary

• Gap Analysis
"""
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Processing
# ==========================================================

if uploaded_file:

    if not api_key:

        st.warning(
            "Please enter your OpenRouter API key."
        )

    else:

        with st.spinner("Analyzing resume..."):

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
                                                # ==========================================================
                # Dashboard Data
                # ==========================================================

                info = analysis.get("candidate_info", {})
                rec = analysis.get("job_recommendation", {})
                ats = analysis.get("ats_analysis", {})

                score = rec.get("confidence_score", 0)
                ats_score = ats.get("overall_score", 0)

                tech = analysis.get("technical_skills", {})
                soft = analysis.get("soft_skills", [])

                skills_found = len(soft)
                for value in tech.values():
                    skills_found += len(value)

                # ==========================================================
                # Dashboard Overview
                # ==========================================================

                st.markdown("## Overview")

                m1, m2, m3, m4 = st.columns(4)

                with m1:
                    st.metric(
                        "ATS Score",
                        ats_score
                    )

                with m2:
                    st.metric(
                        "Match",
                        f"{score}%"
                    )

                with m3:
                    st.metric(
                        "Skills",
                        skills_found
                    )

                with m4:
                    st.metric(
                        "Recommended Role",
                        rec.get("role", "-")
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                # ==========================================================
                # Profile + Recommendation
                # ==========================================================

                left, right = st.columns([1.1, 1])

                # -----------------------------
                # Candidate Profile
                # -----------------------------

                with left:

                    with st.container(border=True):

                        st.subheader("Candidate Profile")

                        st.write(
                            "**Name**",
                            info.get("name", "-")
                        )

                        st.write(
                            "**Email**",
                            info.get("email", "-")
                        )

                        education = info.get(
                            "education",
                            []
                        )

                        if education:

                            with st.expander(
                                "Education",
                                expanded=True
                            ):

                                for edu in education:

                                    st.markdown(
                                        f"""
**{edu.get('degree','')}**

{edu.get('branch','')}

{edu.get('year','')}
"""
                                    )

                        experience = info.get(
                            "experience",
                            []
                        )

                        if experience:

                            with st.expander("Experience"):

                                for exp in experience:

                                    st.markdown(
                                        f"""
**{exp.get('role','')}**

{exp.get('company','')}

{exp.get('duration','')}
"""
                                    )

                # -----------------------------
                # Recommendation
                # -----------------------------

                with right:

                    with st.container(border=True):

                        st.subheader("Job Recommendation")

                        st.metric(
                            "Best Fit",
                            rec.get("role", "-")
                        )

                        st.progress(score / 100)

                        st.caption(
                            f"Confidence Score • {score}%"
                        )

                        st.info(
                            rec.get("reason", "")
                        )

                st.markdown("<br>", unsafe_allow_html=True)

                                # ==========================================================
                # ATS Analysis + Professional Summary
                # ==========================================================

                left, right = st.columns([1, 2])

                with left:

                    with st.container(border=True):

                        st.subheader("ATS Analysis")

                        if ats_score >= 85:
                            verdict = "Excellent"
                        elif ats_score >= 70:
                            verdict = "Strong"
                        elif ats_score >= 50:
                            verdict = "Average"
                        else:
                            verdict = "Needs Improvement"

                        st.markdown(
                            f"""
<div class="ats-score-card">

<h1>{ats_score}</h1>

<p>{verdict}</p>

</div>
""",
                            unsafe_allow_html=True
                        )

                        st.metric(
                            "Keyword Match",
                            f"{ats.get('keyword_match_percentage',0)}%"
                        )

                with right:

                    with st.container(border=True):

                        st.subheader("Professional Summary")

                        st.write(
                            analysis.get(
                                "professional_summary",
                                "Summary not available."
                            )
                        )

                st.markdown("<br>", unsafe_allow_html=True)

                # ==========================================================
                # Skills
                # ==========================================================

                st.subheader("Skills")

                tech_col, soft_col = st.columns(2)

                # ------------------------------------
                # Technical Skills
                # ------------------------------------

                with tech_col:

                    with st.container(border=True):

                        st.markdown("#### Technical Skills")

                        tech = analysis.get(
                            "technical_skills",
                            {}
                        )

                        if tech:

                            for category, skills in tech.items():

                                if skills:

                                    st.caption(
                                        category.replace(
                                            "_",
                                            " "
                                        ).title()
                                    )

                                    badges = "".join(
                                        [
                                            f"<span class='skill-badge'>{skill}</span>"
                                            for skill in skills
                                        ]
                                    )

                                    st.markdown(
                                        badges,
                                        unsafe_allow_html=True
                                    )

                # ------------------------------------
                # Soft Skills
                # ------------------------------------

                with soft_col:

                    with st.container(border=True):

                        st.markdown("#### Soft Skills")

                        soft = analysis.get(
                            "soft_skills",
                            []
                        )

                        if soft:

                            badges = "".join(
                                [
                                    f"<span class='skill-badge'>{skill}</span>"
                                    for skill in soft
                                ]
                            )

                            st.markdown(
                                badges,
                                unsafe_allow_html=True
                            )

                        else:

                            st.write(
                                "No soft skills identified."
                            )

                st.markdown("<br>", unsafe_allow_html=True)

                
                                
                                    # ==========================================================
                # Gap Analysis
                # ==========================================================

                st.subheader("Gap Analysis")

                tab1, tab2, tab3 = st.tabs(
                    [
                        "Missing Skills",
                        "Strengths",
                        "Recommendations"
                    ]
                )

                # ----------------------------------------------------------
                # Missing Skills
                # ----------------------------------------------------------

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

                        st.markdown("#### High Priority Skills")

                        badges = "".join(
                            [
                                f"<span class='skill-badge'>{skill}</span>"
                                for skill in high_priority
                            ]
                        )

                        st.markdown(
                            badges,
                            unsafe_allow_html=True
                        )

                    else:

                        st.success(
                            "No major missing skills identified."
                        )

                    learning_path = missing.get(
                        "suggested_learning_path",
                        ""
                    )

                    if learning_path:

                        st.markdown("#### Suggested Learning Path")

                        st.info(
                            learning_path
                        )

                # ----------------------------------------------------------
                # Strengths
                # ----------------------------------------------------------

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
                            "No strengths available."
                        )

                # ----------------------------------------------------------
                # Recommendations
                # ----------------------------------------------------------

                with tab3:

                    weaknesses = ats.get(
                        "weaknesses",
                        []
                    )

                    if weaknesses:

                        st.markdown("#### Areas to Improve")

                        for item in weaknesses:

                            st.warning(item)

                    suggestions = ats.get(
                        "improvement_suggestions",
                        []
                    )

                    if suggestions:

                        st.markdown("#### Recommended Actions")

                        for i, tip in enumerate(
                            suggestions,
                            start=1
                        ):

                            st.write(
                                f"{i}. {tip}"
                            )

                    else:

                        st.success(
                            "No additional recommendations."
                        )

                st.markdown("<br>", unsafe_allow_html=True)

                # ==========================================================
                # Footer
                # ==========================================================

                st.divider()

                st.caption(
                    "Resume Intelligence • AI-powered resume analysis and ATS evaluation."
                )
