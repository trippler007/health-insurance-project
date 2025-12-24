import streamlit as st

def show_home():
    st.markdown("""
    <div class="page-title">InsureSense</div>
    <div class="page-subtitle">Intelligent Medical Insurance Cost Estimation</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #ffffff; font-size: 15px; line-height: 1.6; margin-bottom: 20px;">
        Estimate your medical insurance costs using data-driven insights based on health, lifestyle, and demographic factors.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card-sm">
            <div class="feature-item-title">Rising Healthcare Costs</div>
            <div class="feature-item-desc">Difficult to estimate without proper data-driven insights.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card-sm">
            <div class="feature-item-title">Lifestyle Impact</div>
            <div class="feature-item-desc">Lifestyle factors significantly impact insurance charges.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card-sm">
            <div class="feature-item-title">Smart Planning</div>
            <div class="feature-item-desc">Data-driven estimates for better financial decisions.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Call to action
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Estimate Your Cost", use_container_width=True, key="home_cta"):
            st.switch_page("pages/estimator.py")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-subtitle">Why Choose InsureSense?</div>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6; margin-bottom: 12px;">
        Our application uses advanced machine learning models trained on real-world healthcare insurance data. 
    </p>
    <p style="color: #ffffff; font-size: 14px; line-height: 1.6;">
        We provide transparent, data-driven estimates that help you understand factors affecting your insurance costs.
    </p>
    """, unsafe_allow_html=True)
