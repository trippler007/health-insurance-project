import streamlit as st
import pandas as pd
import joblib
import os
from pathlib import Path

def show_estimator():
    st.markdown("""
    <div class="page-title">Cost Estimator</div>
    <div class="page-subtitle">Provide your details to receive an estimated insurance cost.</div>
    """, unsafe_allow_html=True)

    # Check if model exists
    model_path = Path("model.joblib")
    model_exists = model_path.exists()

    if not model_exists:
        st.warning("Model file not found. Please ensure model.joblib is in the root directory.")

    st.markdown("""
    <div class="section-title">Personal Information</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<label class="label-text">Age (years)</label>', unsafe_allow_html=True)
        age = st.slider("Age", 18, 100, 30, key="age_input", label_visibility="collapsed")

    with col2:
        st.markdown('<label class="label-text">Gender</label>', unsafe_allow_html=True)
        sex = st.selectbox("Gender", ["Male", "Female"], key="sex_input", label_visibility="collapsed")

    st.markdown("""
    <div class="section-title">Health Metrics</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<label class="label-text">Height (cm)</label>', unsafe_allow_html=True)
        height = st.slider("Height", 140, 210, 170, key="height_input", label_visibility="collapsed")

    with col2:
        st.markdown('<label class="label-text">Weight (kg)</label>', unsafe_allow_html=True)
        weight = st.slider("Weight", 40, 150, 70, key="weight_input", label_visibility="collapsed")

    st.markdown("""
    <div class="section-title">Lifestyle & Region</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<label class="label-text">Dependents</label>', unsafe_allow_html=True)
        children = st.number_input("Dependents", 0, 10, 0, key="children_input", label_visibility="collapsed")

    with col2:
        st.markdown('<label class="label-text">Smoking Status</label>', unsafe_allow_html=True)
        smoker = st.selectbox("Smoking", ["No", "Yes"], key="smoker_input", label_visibility="collapsed")

    with col3:
        st.markdown('<label class="label-text">Region</label>', unsafe_allow_html=True)
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"], key="region_input", label_visibility="collapsed")

    # Calculate BMI
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Prepare input data
    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex.lower()],
        "bmi": [bmi],
        "children": [int(children)],
        "smoker": ["yes" if smoker == "Yes" else "no"],
        "region": [region.lower()]
    })

    st.markdown("<br>", unsafe_allow_html=True)

    # Prediction button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Generate Estimate", use_container_width=True, key="estimate_btn"):
            if model_exists:
                try:
                    model = joblib.load(model_path)
                    prediction = model.predict(input_df)[0]
                    
                    st.markdown("""
                    <div class="section-title">Estimated Outcome</div>
                    """, unsafe_allow_html=True)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("""
                        <div class="card-sm">
                            <div style="color: #ffffff; font-size: 12px; margin-bottom: 6px;">Body Mass Index</div>
                            <div class="secondary-value">{:.2f}</div>
                        </div>
                        """.format(bmi), unsafe_allow_html=True)

                    with col2:
                        st.markdown("""
                        <div class="card-sm">
                            <div style="color: #ffffff; font-size: 12px; margin-bottom: 6px;">Annual Insurance Cost</div>
                            <div class="result-value">${:,.2f}</div>
                        </div>
                        """.format(prediction), unsafe_allow_html=True)

                    st.markdown("""
                    <div class="note-text">
                        This estimation is generated using a machine learning model trained on historical insurance data. Actual costs may vary.
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error loading model: {e}")
            else:
                st.info("Demo Mode: Create a model.joblib file to enable predictions.")
