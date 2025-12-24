import streamlit as st

def show_insights():
    st.markdown("""
    <div class="page-title">Key Cost Factors</div>
    <div class="page-subtitle">Understanding what drives your insurance costs.</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Factors Affecting Insurance Cost</div>
        <p style="color: #d1d5db; line-height: 1.8;">
            Multiple factors influence your medical insurance costs. Learn how each one impacts your premium:
        </p>
    </div>
    """, unsafe_allow_html=True)

    factors = [
        {
            "name": "Age",
            "desc": "Older age generally correlates with higher insurance costs due to increased healthcare utilization and risk factors."
        },
        {
            "name": "Smoking Status",
            "desc": "Smoking is one of the strongest contributors to higher insurance costs, with significant premiums for smokers."
        },
        {
            "name": "Body Mass Index (BMI)",
            "desc": "Higher BMI often increases insurance costs due to associated health risks and medical conditions."
        },
        {
            "name": "Number of Dependents",
            "desc": "More dependents increase the total coverage needs, which impacts the overall insurance cost."
        },
        {
            "name": "Geographic Region",
            "desc": "Insurance costs vary by location due to differences in healthcare services, providers, and cost of living."
        },
        {
            "name": "Health History",
            "desc": "Pre-existing conditions and medical history are significant factors in determining insurance premiums."
        }
    ]

    for factor in factors:
        st.markdown(f"""
        <div class="factor-card">
            <div class="factor-name">{factor['name']}</div>
            <div class="factor-desc">{factor['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Major Cost Drivers</div>
        <p style="color: #d1d5db; line-height: 1.8;">
            <span class="highlight">Smoking and BMI</span> are among the strongest contributors to increased insurance costs. 
            A combination of smoking status and high BMI can result in significantly higher premiums compared to non-smokers with healthy BMI.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Lifestyle Improvements</div>
        <p style="color: #d1d5db; line-height: 1.8;">
            Making healthy lifestyle changes such as quitting smoking and maintaining a healthy BMI can significantly reduce your insurance costs. 
            These changes not only improve your insurance premiums but also enhance your overall health and well-being.
        </p>
    </div>
    """, unsafe_allow_html=True)
