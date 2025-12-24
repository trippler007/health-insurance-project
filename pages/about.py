import streamlit as st

def show_about():
    st.markdown("# About InsureSense")
    st.markdown('<p class="subtitle">Medical Insurance Cost Estimation System.</p>', unsafe_allow_html=True)

    st.markdown("## Overview")
    st.markdown("""
    <p>InsureSense is a machine learning application that demonstrates data science applications in predicting healthcare insurance costs. This project uses demographic and lifestyle attributes to estimate medical insurance charges based on historical data patterns.</p>
    """, unsafe_allow_html=True)

    st.markdown("## Technology Stack")
    
    col1, col2 = st.columns(2)
    tech_stack = [
        ("Python", "Core programming language"),
        ("Pandas & NumPy", "Data processing and numerical computing"),
        ("Scikit-learn", "Machine learning algorithms"),
        ("Streamlit", "Web application framework"),
        ("Joblib", "Model serialization"),
    ]

    for i, (tech, desc) in enumerate(tech_stack):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"**{tech}**")
            st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Dataset")
    st.markdown("""
    <p>Uses the Healthcare Insurance Dataset from Kaggle, containing structured information about individuals' characteristics and their medical insurance charges.</p>
    """, unsafe_allow_html=True)

    st.markdown("## Use Cases")
    
    use_cases = [
        ("Educational", "Learn how ML applies to real-world healthcare data"),
        ("Financial Planning", "Estimate insurance costs for personal decisions"),
        ("Healthcare Analytics", "Understand insurance cost factors"),
        ("Portfolio", "Showcase data science and ML skills")
    ]

    col1, col2 = st.columns(2)
    for i, (usecase, desc) in enumerate(use_cases):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"**{usecase}**")
            st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
