import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .skill-badge {
        display: inline-block;
        padding: 4px 12px;
        margin: 4px;
        border-radius: 15px;
        background-color: #e9ecef;
        color: #495057;
        font-weight: 500;
        font-size: 0.85rem;
    }
    .ats-score-card {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
