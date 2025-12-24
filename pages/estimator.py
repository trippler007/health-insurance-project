import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

def show_estimator():
    st.markdown("# Cost Estimator")
    st.markdown('<p class="subtitle">Provide your details to receive an estimated insurance cost.</p>', unsafe_allow_html=True)

    # Check if model exists
    model_path = Path("model.joblib")
    model_exists = model_path.exists()

    if not model_exists:
        st.warning("Model file not found. Using demo mode.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Personal")
        age = st.slider("Age (years)", 18, 100, 30, key="age")
        sex = st.selectbox("Gender", ["Male", "Female"], key="sex")
        children = st.number_input("Dependents", 0, 10, 0, key="children")

    with col2:
        st.markdown("## Health & Region")
        height = st.slider("Height (cm)", 140, 210, 170, key="height")
        weight = st.slider("Weight (kg)", 40, 150, 70, key="weight")
        smoker = st.selectbox("Smoking Status", ["No", "Yes"], key="smoker")

    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"], key="region")

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

    st.markdown("---")

    if st.button("Generate Estimate", use_container_width=True, key="estimate_btn"):
        if model_exists:
            try:
                model = joblib.load(model_path)
                prediction = model.predict(input_df)[0]
                
                st.markdown("## Your Estimate")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("""
                    <div class="result-card">
                        <div class="metric-label">Body Mass Index</div>
                        <div class="secondary-metric">{:.1f}</div>
                    </div>
                    """.format(bmi), unsafe_allow_html=True)

                with col2:
                    st.markdown("""
                    <div class="result-card">
                        <div class="metric-label">Annual Insurance Cost</div>
                        <div class="metric-value">${:,.0f}</div>
                    </div>
                    """.format(prediction), unsafe_allow_html=True)

                st.markdown("""
                <p class="note">This estimation is generated using a machine learning model trained on historical insurance data. Actual costs may vary based on additional factors not included in this model.</p>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error loading model: {e}")
        else:
            st.info("Demo Mode: Add a model.joblib file to enable predictions.")
