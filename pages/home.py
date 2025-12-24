import streamlit as st

def show_home():
    st.markdown("""
    <div class="page-title">InsureSense</div>
    <div class="page-subtitle">Intelligent Medical Insurance Cost Estimation</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-title">Estimate your medical insurance costs using data-driven insights based on health, lifestyle, and demographic factors.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="glass-card-sm">
            <div class="feature-item-title">Rising Healthcare Costs</div>
            <div class="feature-item-desc">Difficult to estimate without proper data-driven insights and analytics.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card-sm">
            <div class="feature-item-title">Lifestyle Impact</div>
            <div class="feature-item-desc">Lifestyle factors significantly impact the insurance charges you pay.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass-card-sm">
            <div class="feature-item-title">Smart Planning</div>
            <div class="feature-item-desc">Data-driven estimates help you make better financial planning decisions.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Call to action
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Estimate Your Insurance Cost", use_container_width=True, key="home_cta"):
            st.session_state.page = "estimator"
            st.switch_page("pages/estimator.py")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <div class="section-subtitle">Why Choose InsureSense?</div>
        <p style="color: #d1d5db; line-height: 1.8; margin-bottom: 16px;">
            Our application uses advanced machine learning models trained on real-world healthcare insurance data. 
            We provide transparent, data-driven estimates that help you understand the factors affecting your insurance costs.
        </p>
        <p style="color: #d1d5db; line-height: 1.8;">
            Whether you are planning your finances or exploring how different lifestyle factors impact your insurance premium, 
            InsureSense provides the insights you need.
        </p>
    </div>
    """, unsafe_allow_html=True)
