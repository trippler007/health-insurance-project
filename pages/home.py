import streamlit as st

def show_home():
    st.markdown("# InsureSense")
    st.markdown('<p class="subtitle">Intelligent Medical Insurance Cost Estimation</p>', unsafe_allow_html=True)

    st.markdown("""
    <p>Estimate your medical insurance costs using data-driven insights based on health, lifestyle, and demographic factors. Our machine learning model analyzes key factors to provide accurate predictions.</p>
    """, unsafe_allow_html=True)

    st.markdown("## Get Started")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("Estimate Your Cost →", use_container_width=True, key="home_cta"):
            st.switch_page("pages/estimator.py")

    st.markdown("---")
    st.markdown("## Why InsureSense?")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Rising Healthcare Costs**")
        st.markdown("<p style='margin-top: 4px;'>Difficult to estimate without proper data-driven insights.</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("**Lifestyle Impact**")
        st.markdown("<p style='margin-top: 4px;'>Lifestyle factors significantly impact insurance charges.</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("**Smart Planning**")
        st.markdown("<p style='margin-top: 4px;'>Data-driven estimates for better financial decisions.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## How It Works")
    st.markdown("""
    <p>Our application uses advanced machine learning models trained on real-world healthcare insurance data. We provide transparent, data-driven estimates that help you understand the factors affecting your insurance costs. Simply input your information, and get an instant prediction.</p>
    """, unsafe_allow_html=True)
