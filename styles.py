import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>

    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"]{
        font-family: 'Inter', sans-serif;
    }

    /* Background */
    .stApp{
        background: linear-gradient(135deg,#0F172A,#1E293B);
        color:white;
    }

    .main{
        padding-top:20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background:#111827;
        border-right:1px solid rgba(255,255,255,.08);
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    /* Cards */
    div[data-testid="stMetric"]{
        background:#1E293B;
        border:1px solid rgba(255,255,255,.08);
        border-radius:18px;
        padding:18px;
        box-shadow:0 8px 24px rgba(0,0,0,.25);
        transition:.3s;
    }

    div[data-testid="stMetric"]:hover{
        transform:translateY(-4px);
        border-color:#3B82F6;
    }

    /* Buttons */
    .stButton>button{
        width:100%;
        background:#2563EB;
        color:white;
        border:none;
        border-radius:10px;
        padding:12px;
        font-weight:600;
    }

    .stButton>button:hover{
        background:#1D4ED8;
    }

    /* Upload box */
    [data-testid="stFileUploader"]{
        border:2px dashed #3B82F6;
        border-radius:18px;
        background:#1E293B;
        padding:15px;
    }

    /* Skill badges */
    .skill-badge{
        display:inline-block;
        padding:8px 16px;
        margin:6px;
        border-radius:30px;
        background:linear-gradient(90deg,#2563EB,#3B82F6);
        color:white;
        font-size:14px;
        font-weight:600;
    }

    /* ATS Card */
    .ats-score-card{
        background:linear-gradient(135deg,#10B981,#059669);
        border-radius:18px;
        padding:30px;
        text-align:center;
        color:white;
        box-shadow:0 10px 25px rgba(16,185,129,.35);
    }

    /* Progress Bar */
    .stProgress > div > div{
        background:#3B82F6;
    }

    /* Tabs */
    button[data-baseweb="tab"]{
        border-radius:10px;
        font-weight:600;
    }

    button[data-baseweb="tab"][aria-selected="true"]{
        background:#2563EB;
        color:white;
    }

    /* Expander */
    details{
        background:#1E293B;
        border-radius:12px;
        border:1px solid rgba(255,255,255,.08);
        padding:8px;
    }

    /* Success */
    .stSuccess{
        border-radius:12px;
    }

    /* Warning */
    .stWarning{
        border-radius:12px;
    }

    /* Error */
    .stError{
        border-radius:12px;
    }

    h1,h2,h3{
        color:white;
        font-weight:700;
    }

    p,label{
        color:#E5E7EB;
    }

    </style>
    """, unsafe_allow_html=True)
