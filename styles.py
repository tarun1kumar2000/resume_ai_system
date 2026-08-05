import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ---------- Background ---------- */

    .stApp{
        background:#F4F7FB;
        color:#1F2937;
    }

    .main{
        padding-top:1rem;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"]{
        background:#FFFFFF;
        border-right:1px solid #E5E7EB;
    }

    /* ---------- Headings ---------- */

    h1,h2,h3{
        color:#111827;
        font-weight:700;
    }

    p,label{
        color:#4B5563;
    }

    /* ---------- Cards ---------- */

    div[data-testid="stMetric"]{

        background:#FFFFFF;

        border:1px solid #E5E7EB;

        border-radius:14px;

        padding:18px;

        box-shadow:0 3px 10px rgba(0,0,0,.05);

        transition:.25s;
    }

    div[data-testid="stMetric"]:hover{

        border-color:#2563EB;

        transform:translateY(-2px);
    }

    /* ---------- File Uploader ---------- */

    [data-testid="stFileUploader"]{

        background:#FFFFFF;

        border:2px dashed #CBD5E1;

        border-radius:16px;

        padding:20px;
    }

    /* ---------- Buttons ---------- */

    .stButton>button{

        background:#2563EB;

        color:white;

        border:none;

        border-radius:10px;

        font-weight:600;

        padding:10px 18px;
    }

    .stButton>button:hover{

        background:#1D4ED8;
    }

    /* ---------- Progress ---------- */

    .stProgress > div > div{

        background:#2563EB;
    }

    /* ---------- Skill Badge ---------- */

    .skill-badge{

        display:inline-block;

        background:#EFF6FF;

        color:#1D4ED8;

        border:1px solid #BFDBFE;

        border-radius:20px;

        padding:6px 14px;

        margin:5px;

        font-size:13px;

        font-weight:500;
    }

    /* ---------- ATS Card ---------- */

    .ats-score-card{

        background:#FFFFFF;

        border:1px solid #E5E7EB;

        border-radius:16px;

        padding:25px;

        text-align:center;

        box-shadow:0 4px 12px rgba(0,0,0,.05);
    }

    .ats-score-card h1{

        color:#2563EB;

        font-size:48px;

        margin:0;
    }

    .ats-score-card p{

        margin-top:8px;

        color:#6B7280;
    }

    /* ---------- Tabs ---------- */

    button[data-baseweb="tab"]{

        border-radius:10px;

        font-weight:600;
    }

    button[data-baseweb="tab"][aria-selected="true"]{

        background:#2563EB;

        color:white;
    }

    /* ---------- Expander ---------- */

    details{

        background:#FFFFFF;

        border:1px solid #E5E7EB;

        border-radius:10px;

        padding:8px;
    }

    /* ---------- Alerts ---------- */

    .stSuccess,
    .stInfo,
    .stWarning,
    .stError{

        border-radius:10px;
    }

    hr{

        border:none;

        border-top:1px solid #E5E7EB;
    }

    </style>
    """, unsafe_allow_html=True)
