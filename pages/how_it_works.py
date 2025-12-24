import streamlit as st

def show_how_it_works():
    st.markdown("""
    <div class="page-title">How It Works</div>
    <div class="page-subtitle">Understanding the science behind InsureSense predictions.</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Our machine learning system applies learned patterns from historical data to estimate insurance costs for new profiles. Here's the step-by-step process:</div>
    </div>
    """, unsafe_allow_html=True)

    steps = [
        {
            "number": "1",
            "title": "Data Collection",
            "desc": "Our dataset contains age, BMI, smoking status, dependents, region, and historical insurance charges from thousands of real-world cases."
        },
        {
            "number": "2",
            "title": "Feature Processing",
            "desc": "Categorical features are encoded into numerical values. BMI is calculated from height and weight measurements to standardize health metrics."
        },
        {
            "number": "3",
            "title": "Model Training",
            "desc": "A supervised machine learning regression model is trained on historical insurance data to learn the relationships between factors and costs."
        },
        {
            "number": "4",
            "title": "Prediction",
            "desc": "User inputs are passed to the trained model, which estimates insurance charges based on patterns learned from historical data."
        }
    ]

    for step in steps:
        st.markdown(f"""
        <div class="glass-card">
            <div class="step-number">{step['number']}</div>
            <div class="step-title">{step['title']}</div>
            <div class="step-desc">{step['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Accuracy and Reliability</div>
        <p style="color: #d1d5db; line-height: 1.8; margin-bottom: 16px;">
            Our model is built using industry-standard machine learning techniques and validated on real-world data. 
            While we strive for high accuracy, estimates are for informational purposes and actual insurance costs may vary.
        </p>
    </div>
    """, unsafe_allow_html=True)
