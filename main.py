import streamlit as st
from pages.home import show_home
from pages.estimator import show_estimator
from pages.how_it_works import show_how_it_works
from pages.insights import show_insights
from pages.about import show_about

# Page configuration
st.set_page_config(
    page_title="InsureSense | Medical Insurance Cost Estimation",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #0f1419;
    color: #ffffff;
}

.main {
    background: transparent;
}

/* Simplified and cleaned up CSS - removed excessive card styles */
.app-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 24px 16px;
}

h1 {
    font-size: 36px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}

h2 {
    font-size: 16px;
    font-weight: 600;
    color: #ffffff;
    margin-top: 16px;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    opacity: 0.9;
}

h3 {
    font-size: 15px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 6px;
}

p {
    color: #e0e0e0;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 12px;
}

.subtitle {
    color: #b0b0b0;
    font-size: 15px;
    margin-bottom: 20px;
    line-height: 1.6;
}

.accent {
    color: #10b981;
    font-weight: 600;
}

/* Minimal card - only for results */
.result-card {
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.2);
    border-radius: 6px;
    padding: 14px;
    margin-bottom: 12px;
}

.metric-label {
    color: #b0b0b0;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}

.metric-value {
    font-size: 32px;
    font-weight: 700;
    color: #10b981;
    letter-spacing: -0.5px;
}

.secondary-metric {
    font-size: 24px;
    font-weight: 700;
    color: #10b981;
}

.note {
    color: #808080;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 8px;
}

/* Input styling */
.stSlider > div > div > div > div {
    color: #ffffff;
}

input, select, textarea {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
}

input::placeholder {
    color: #606060 !important;
}

/* Radio and checkbox */
.stRadio > label {
    color: #ffffff !important;
    font-size: 14px !important;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: #0a0d12;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    padding: 0;
}

.stRadio {
    padding-left: 0 !important;
}

/* Button styling */
button {
    border-radius: 6px !important;
}

[data-testid="baseButton-primary"] {
    background: #10b981 !important;
    color: #ffffff !important;
}

[data-testid="baseButton-primary"]:hover {
    background: #059669 !important;
}

/* Expander styling */
.streamlit-expanderHeader {
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="app-container">', unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Estimator", "How It Works", "Factors", "About"],
    label_visibility="visible"
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
