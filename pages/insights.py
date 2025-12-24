import streamlit as st

def show_insights():
    st.markdown("# Key Cost Factors")
    st.markdown('<p class="subtitle">Understanding what drives your insurance costs.</p>', unsafe_allow_html=True)

    st.markdown("""
    <p>Multiple factors influence your medical insurance costs. Learn how each one impacts your premium:</p>
    """, unsafe_allow_html=True)

    factors = [
        ("Age", "Older age correlates with higher costs due to increased healthcare needs."),
        ("Smoking Status", "Smoking is one of the strongest contributors to higher insurance costs."),
        ("BMI", "Higher body mass index increases costs due to associated health risks."),
        ("Dependents", "More dependents increase coverage needs and overall insurance cost."),
        ("Geographic Region", "Insurance costs vary by location due to regional healthcare differences."),
        ("Health History", "Pre-existing conditions and medical history significantly affect premiums.")
    ]

    col1, col2 = st.columns(2)
    for i, (name, desc) in enumerate(factors):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"**{name}**")
            st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Major Cost Drivers")
    st.markdown("""
    <p><span class="accent">Smoking and BMI</span> are the strongest contributors to increased insurance costs. A combination of smoking and high BMI can result in significantly higher premiums.</p>
    """, unsafe_allow_html=True)

    st.markdown("## Improve Your Costs")
    st.markdown("""
    <p>Making healthy lifestyle changes such as quitting smoking and maintaining a healthy BMI can significantly reduce your insurance costs over time.</p>
    """, unsafe_allow_html=True)
