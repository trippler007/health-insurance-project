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
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0e27;
}

[data-testid="stAppViewContainer"] {
    background: #0a0e27;
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
    padding: 30px 20px;
}

.page-title {
    font-size: 42px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.page-subtitle {
    font-size: 16px;
    color: #ffffff;
    margin-bottom: 24px;
    line-height: 1.5;
}

.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
    margin-top: 20px;
}

.section-subtitle {
    font-size: 16px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 12px;
    margin-top: 16px;
}

.label-text {
    color: #ffffff;
    font-weight: 500;
    font-size: 14px;
    margin-bottom: 6px;
    display: block;
}

.result-value {
    font-size: 40px;
    font-weight: 700;
    color: #22d3ee;
    letter-spacing: -1px;
}

.secondary-value {
    font-size: 26px;
    font-weight: 700;
    color: #22d3ee;
}

.note-text {
    font-size: 13px;
    color: #ffffff;
    line-height: 1.5;
    margin-top: 8px;
}

.card {
    background: rgba(6, 182, 212, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
}

.card-sm {
    background: rgba(6, 182, 212, 0.08);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 12px;
}

.feature-item-title {
    font-size: 15px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 6px;
}

.feature-item-desc {
    font-size: 13px;
    color: #ffffff;
    line-height: 1.5;
}

.step-number {
    font-size: 28px;
    font-weight: 700;
    color: #22d3ee;
    margin-bottom: 6px;
}

.step-title {
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 6px;
}

.step-desc {
    font-size: 13px;
    color: #ffffff;
    line-height: 1.5;
}

.factor-name {
    font-size: 15px;
    font-weight: 700;
    color: #22d3ee;
    margin-bottom: 6px;
}

.factor-desc {
    font-size: 13px;
    color: #ffffff;
    line-height: 1.5;
}

.highlight {
    color: #22d3ee;
    font-weight: 600;
}

[data-testid="stSidebar"] {
    background: #0f1629;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    padding: 10px 0;
}

.stRadio > label {
    color: #ffffff !important;
    font-size: 14px !important;
}

.stRadio > label > div {
    font-size: 14px;
}

input, select, textarea {
    background: rgba(34, 211, 238, 0.08) !important;
    border: 1px solid rgba(34, 211, 238, 0.2) !important;
    color: #ffffff !important;
}

input::placeholder {
    color: #888888 !important;
}

button {
    color: #ffffff !important;
}

p {
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="app-container">', unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    ["Home", "Estimator", "How It Works", "Factors", "About"],
    label_visibility="collapsed"
)

# Route to pages
if page == "Home":
    show_home()
elif page == "Estimator":
    show_estimator()
elif page == "How It Works":
    show_how_it_works()
elif page == "Factors":
    show_insights()
elif page == "About":
    show_about()

st.markdown('</div>', unsafe_allow_html=True)
