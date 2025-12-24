import streamlit as st

def show_how_it_works():
    st.markdown("# How It Works")
    st.markdown('<p class="subtitle">Understanding the science behind InsureSense predictions.</p>', unsafe_allow_html=True)

    st.markdown("""
    <p>Our machine learning system learns patterns from historical data to estimate insurance costs for new profiles. Here's the step-by-step process:</p>
    """, unsafe_allow_html=True)

    st.markdown("## Step 1: Data Collection")
    st.markdown("<p>Our dataset contains age, BMI, smoking status, dependents, region, and historical insurance charges.</p>", unsafe_allow_html=True)

    st.markdown("## Step 2: Feature Processing")
    st.markdown("<p>Categorical features are encoded into numerical values. BMI is calculated from height and weight.</p>", unsafe_allow_html=True)

    st.markdown("## Step 3: Model Training")
    st.markdown("<p>A supervised machine learning regression model is trained on historical insurance data using advanced algorithms.</p>", unsafe_allow_html=True)

    st.markdown("## Step 4: Prediction")
    st.markdown("<p>User inputs are passed to the trained model to estimate insurance charges instantly.</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Accuracy & Reliability")
    st.markdown("""
    <p>Our model is built using industry-standard machine learning techniques and validated on real-world data. Predictions are for informational purposes and may vary from actual costs.</p>
    """, unsafe_allow_html=True)
