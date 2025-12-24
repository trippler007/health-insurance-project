import streamlit as st

def show_how_it_works():
    st.markdown("""
    <div class="page-title">How It Works</div>
    <div class="page-subtitle">Understanding the science behind InsureSense predictions.</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 20px;">
        Our machine learning system learns patterns from historical data to estimate insurance costs for new profiles.
    </p>
    """, unsafe_allow_html=True)

    steps = [
        {
            "number": "1",
            "title": "Data Collection",
            "desc": "Our dataset contains age, BMI, smoking status, dependents, region, and historical insurance charges."
        },
        {
            "number": "2",
            "title": "Feature Processing",
            "desc": "Categorical features are encoded into numerical values. BMI is calculated from height and weight."
        },
        {
            "number": "3",
            "title": "Model Training",
            "desc": "A supervised machine learning regression model is trained on historical insurance data."
        },
        {
            "number": "4",
            "title": "Prediction",
            "desc": "User inputs are passed to the trained model to estimate insurance charges."
        }
    ]

    for step in steps:
        st.markdown(f"""
        <div class="card">
            <div class="step-number">{step['number']}</div>
            <div class="step-title">{step['title']}</div>
            <div class="step-desc">{step['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Accuracy and Reliability</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6;">
        Our model is built using industry-standard machine learning techniques and validated on real-world data. Estimates are for informational purposes.
    </p>
    """, unsafe_allow_html=True)
