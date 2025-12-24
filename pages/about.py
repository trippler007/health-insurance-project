import streamlit as st

def show_about():
    st.markdown("""
    <div class="page-title">About the Project</div>
    <div class="page-subtitle">InsureSense Medical Insurance Cost Estimation System.</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Project Overview</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
        InsureSense is a machine learning application that demonstrates the practical application of data science in predicting healthcare insurance costs. This project uses demographic and lifestyle attributes to estimate medical insurance charges based on historical data patterns.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Technology Stack</div>
    """, unsafe_allow_html=True)

    tech_stack = [
        ("Python", "Core programming language"),
        ("Pandas & NumPy", "Data processing and numerical computing"),
        ("Scikit-learn", "Machine learning algorithms and model training"),
        ("Streamlit", "Interactive web application framework"),
        ("Joblib", "Model serialization and persistence")
    ]

    for tech, desc in tech_stack:
        st.markdown(f"""
        <div class="card-sm">
            <div class="factor-name">{tech}</div>
            <div class="factor-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Dataset</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
        The application uses the Healthcare Insurance Dataset from Kaggle, which contains structured information about individuals' characteristics and their medical insurance charges.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Use Cases</div>
    """, unsafe_allow_html=True)

    use_cases = [
        ("Educational", "Learn how machine learning applies to real-world healthcare data"),
        ("Financial Planning", "Estimate insurance costs for better personal financial decisions"),
        ("Healthcare Analytics", "Understand factors affecting medical insurance charges"),
        ("Portfolio Demonstration", "Showcase data science and machine learning skills")
    ]

    for usecase, desc in use_cases:
        st.markdown(f"""
        <div class="card-sm">
            <div class="factor-name">{usecase}</div>
            <div class="factor-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Project Goals</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6;">
        This project aims to bridge the gap between healthcare data and consumer understanding by providing transparent, data-driven insights into insurance cost estimation.
    </p>
    """, unsafe_allow_html=True)
