import streamlit as st

def show_insights():
    st.markdown("""
    <div class="page-title">Key Cost Factors</div>
    <div class="page-subtitle">Understanding what drives your insurance costs.</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">
        Multiple factors influence your medical insurance costs. Learn how each one impacts your premium:
    </p>
    """, unsafe_allow_html=True)

    factors = [
        {
            "name": "Age",
            "desc": "Older age generally correlates with higher insurance costs due to increased healthcare needs."
        },
        {
            "name": "Smoking Status",
            "desc": "Smoking is one of the strongest contributors to higher insurance costs."
        },
        {
            "name": "Body Mass Index (BMI)",
            "desc": "Higher BMI often increases insurance costs due to associated health risks."
        },
        {
            "name": "Number of Dependents",
            "desc": "More dependents increase the total coverage needs and overall insurance cost."
        },
        {
            "name": "Geographic Region",
            "desc": "Insurance costs vary by location due to differences in healthcare services and costs."
        },
        {
            "name": "Health History",
            "desc": "Pre-existing conditions and medical history are significant factors in determining premiums."
        }
    ]

    for factor in factors:
        st.markdown(f"""
        <div class="card">
            <div class="factor-name">{factor['name']}</div>
            <div class="factor-desc">{factor['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Major Cost Drivers</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 12px;">
        <span class="highlight">Smoking and BMI</span> are among the strongest contributors to increased insurance costs. A combination of smoking and high BMI can result in significantly higher premiums.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-subtitle">Lifestyle Improvements</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6;">
        Making healthy lifestyle changes such as quitting smoking and maintaining a healthy BMI can significantly reduce your insurance costs.
    </p>
    """, unsafe_allow_html=True)
