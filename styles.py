import streamlit as st

def apply_custom_css():
    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

*{
    font-family:'Inter',sans-serif;
}

/* =========================
   PAGE
========================= */

.stApp{
    background:#F8FAFC;
    color:#111827;
}

.block-container{
    max-width:1200px;
    padding-top:1.8rem;
    padding-bottom:2rem;
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E5E7EB;
}

section[data-testid="stSidebar"] .block-container{
    padding-top:1.5rem;
}

/* =========================
   HEADINGS
========================= */

h1{
    font-size:2.2rem;
    font-weight:800;
    color:#111827;
    margin-bottom:.3rem;
}

h2{
    font-weight:700;
}

h3{
    font-weight:600;
}

p,label{
    color:#6B7280;
}

/* =========================
   METRIC CARDS
========================= */

div[data-testid="stMetric"]{

    background:#FFFFFF;

    border:1px solid #E5E7EB;

    border-radius:16px;

    padding:18px;

    transition:.25s;

    box-shadow:0 8px 25px rgba(15,23,42,.04);

}

div[data-testid="stMetric"]:hover{

    transform:translateY(-3px);

    border-color:#2563EB;

    box-shadow:0 15px 35px rgba(37,99,235,.08);

}

/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"]{

    background:#FFFFFF;

    border:2px dashed #93C5FD;

    border-radius:18px;

    padding:30px;

    transition:.25s;

}

[data-testid="stFileUploader"]:hover{

    border-color:#2563EB;

    background:#F9FBFF;

}

/* =========================
   BUTTONS
========================= */

.stButton>button{

    width:100%;

    height:46px;

    border:none;

    border-radius:12px;

    background:#2563EB;

    color:white;

    font-weight:600;

}

.stButton>button:hover{

    background:#1D4ED8;

}

/* =========================
   PROGRESS BAR
========================= */

.stProgress > div > div{

    background:#2563EB;

}

/* =========================
   SKILL CHIP
========================= */

.skill-badge{

    display:inline-block;

    padding:7px 14px;

    margin:5px;

    border-radius:999px;

    background:#EFF6FF;

    border:1px solid #BFDBFE;

    color:#1D4ED8;

    font-size:13px;

    font-weight:600;

}

/* =========================
   ATS CARD
========================= */

.ats-score-card{

    background:white;

    border:1px solid #E5E7EB;

    border-radius:18px;

    padding:28px;

    text-align:center;

    box-shadow:0 10px 25px rgba(0,0,0,.04);

}

.ats-score-card h1{

    font-size:60px;

    color:#2563EB;

    margin-bottom:4px;

}

.ats-score-card p{

    margin:0;

    color:#6B7280;

}

/* =========================
   TABS
========================= */

button[data-baseweb="tab"]{

    border-radius:10px;

    font-weight:600;

    padding:10px 18px;

}

button[data-baseweb="tab"][aria-selected="true"]{

    background:#2563EB;

    color:white;

}

/* =========================
   EXPANDER
========================= */

details{

    border:1px solid #E5E7EB;

    border-radius:12px;

    background:white;

    padding:10px;

    margin-bottom:10px;

}

/* =========================
   ALERTS
========================= */

.stSuccess,
.stWarning,
.stInfo,
.stError{

    border-radius:12px;

}

/* =========================
   HERO CARD
========================= */

.hero{

    background:white;

    border-radius:18px;

    border:1px solid #E5E7EB;

    padding:26px;

    margin-bottom:25px;

    box-shadow:0 10px 25px rgba(15,23,42,.04);

}

.hero h2{

    margin-bottom:8px;

    color:#111827;

}

.hero p{

    margin:0;

    color:#6B7280;

}

/* =========================
   DIVIDER
========================= */

hr{

    border:none;

    border-top:1px solid #E5E7EB;

}

/* =========================
   MOBILE
========================= */

@media (max-width:768px){

.block-container{

padding:1rem;

}

h1{

font-size:1.8rem;

}

[data-testid="stFileUploader"]{

padding:20px;

}

}

</style>
""", unsafe_allow_html=True)
