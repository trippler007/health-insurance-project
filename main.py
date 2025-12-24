import streamlit as st
import pandas as pd
from pages.home import show_home
from pages.estimator import show_estimator
from pages.how_it_works import show_how_it_works
from pages.insights import show_insights
from pages.about import show_about

# Page configuration
st.set_page_config(
    page_title="InsureSense | Medical Insurance Cost Estimation",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
}

.main {
    background: transparent;
}

.stMainBlockContainer {
    background: transparent;
}

.app-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

.page-title {
    font-size: 48px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 16px;
    letter-spacing: -0.5px;
}

.page-subtitle {
    font-size: 18px;
    color: #d1d5db;
    margin-bottom: 40px;
    line-height: 1.6;
}

.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.4);
    margin-bottom: 24px;
}

.glass-card-sm {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 24px;
}

.section-subtitle {
    font-size: 16px;
    font-weight: 600;
    color: #e5e7eb;
    margin-bottom: 16px;
    margin-top: 24px;
}

.label-text {
    color: #d1d5db;
    font-weight: 500;
    font-size: 14px;
    margin-bottom: 8px;
    display: block;
}

.result-value {
    font-size: 42px;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: -1px;
}

.secondary-value {
    font-size: 28px;
    font-weight: 700;
    color: #fbbf24;
}

.note-text {
    font-size: 13px;
    color: #9ca3af;
    line-height: 1.5;
    margin-top: 12px;
}

.cta-button {
    background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
    color: white;
    font-weight: 600;
    padding: 14px 32px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 16px;
}

.cta-button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 12px 24px rgba(6, 182, 212, 0.3);
}

.feature-item {
    padding: 24px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    margin-bottom: 16px;
}

.feature-item-title {
    font-size: 16px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 8px;
}

.feature-item-desc {
    font-size: 14px;
    color: #d1d5db;
    line-height: 1.6;
}

.step-number {
    font-size: 36px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 8px;
}

.step-title {
    font-size: 18px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 8px;
}

.step-desc {
    font-size: 14px;
    color: #d1d5db;
    line-height: 1.6;
}

.factor-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}

.factor-name {
    font-size: 16px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 8px;
}

.factor-desc {
    font-size: 14px;
    color: #d1d5db;
    line-height: 1.6;
}

.highlight {
    color: #fbbf24;
    font-weight: 600;
}

.navigation {
    display: flex;
    gap: 16px;
    margin-top: 40px;
    justify-content: center;
    flex-wrap: wrap;
}

.nav-button {
    padding: 10px 20px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: #d1d5db;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.nav-button:hover {
    background: rgba(255, 255, 255, 0.15);
    color: #f9fafb;
}

[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
}

.stSlider [data-testid="stTickBar"] {
    background: rgba(6, 182, 212, 0.3);
}

.stNumberInput input, .stSelectbox select, .stTextInput input {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #f9fafb !important;
}

</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Cost Estimator", "How It Works", "Insights & Factors", "About the Project"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='color: #9ca3af; font-size: 12px; text-align: center;'>"
    "InsureSense v1.0<br>Medical Insurance Cost Estimation"
    "</p>",
    unsafe_allow_html=True
)

# Route to pages
if page == "Home":
    show_home()
elif page == "Cost Estimator":
    show_estimator()
elif page == "How It Works":
    show_how_it_works()
elif page == "Insights & Factors":
    show_insights()
elif page == "About the Project":
    show_about()

st.markdown('</div>', unsafe_allow_html=True)
