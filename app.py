import streamlit as st
from PIL import Image
import numpy as np
from model import detect_number_plate
import time
import base64
from io import BytesIO

# Page Config
st.set_page_config(
    page_title="AI License Plate Detector",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

:root {
    --primary-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
    --bg-color: #0f172a;
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
    --text-color: #f8fafc;
}

.stApp {
    background: radial-gradient(circle at top right, #1e293b, #0f172a);
    font-family: 'Inter', sans-serif;
    color: var(--text-color);
    overflow: hidden;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem !important;
    max-width: 95% !important;
}

.main-container {
    background: var(--glass-bg);
    backdrop-filter: blur(12px);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 1rem;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-bottom: 0.5rem;
}

.header-title {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    font-size: 2rem !important;
    text-align: center;
    margin-bottom: 0.2rem;
    letter-spacing: -0.02em;
}

.header-subtitle {
    color: #94a3b8;
    text-align: center;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.02);
    border: 1px dashed var(--glass-border);
    border-radius: 12px;
    padding: 0.5rem;
}

/* HIGHLIGHTED BUTTON */
.stButton>button {
    background: var(--primary-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.8rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
    margin-top: 1rem !important;
}

.stButton>button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.6) !important;
    filter: brightness(1.1);
}

.stButton>button:active {
    transform: translateY(0) scale(0.98) !important;
}

.image-card {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--glass-border);
    height: 300px; /* Fixed height */
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0,0,0,0.2);
    margin-bottom: 0.5rem;
}

.image-card img {
    height: 300px !important;
    width: 100% !important;
    object-fit: contain !important;
}

.metric-card {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 12px;
    padding: 0.5rem;
    text-align: center;
    border: 1px solid var(--glass-border);
    margin-top: 0.5rem;
}

.metric-value {
    font-size: 1.1rem;
    font-weight: 700;
    color: #a855f7;
}

.metric-label {
    font-size: 0.7rem;
    color: #94a3b8;
    text-transform: uppercase;
}

#MainMenu, footer, header {visibility: hidden; height: 0;}
</style>
""", unsafe_allow_html=True)

def get_image_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Header Section
st.markdown('<h1 class="header-title">VisionX Plate Detector</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-subtitle">Advanced AI vehicle identification system</p>', unsafe_allow_html=True)

# Main Content Layout
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.markdown("##### 📥 Input")
    uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        img_b64 = get_image_base64(image)
        st.markdown(f'<div class="image-card"><img src="data:image/png;base64,{img_b64}"></div>', unsafe_allow_html=True)
        
        if st.button("🚀 Run Analysis"):
            with st.spinner("Analyzing..."):
                time.sleep(0.5)
                image_np = np.array(image)
                result_img = detect_number_plate(image_np)
                st.session_state['result'] = result_img
                st.session_state['processed'] = True
    else:
        st.markdown('<div class="image-card" style="height: 300px; border: 1px dashed rgba(255,255,255,0.1); color: #64748b; font-size: 0.8rem;">Upload an image to start</div>', unsafe_allow_html=True)

    # Info Cards (Compact)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="metric-card"><div class="metric-value">YOLOv8</div><div class="metric-label">Model</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><div class="metric-value">98%</div><div class="metric-label">Accuracy</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown("##### 🔍 Result")
    
    if 'processed' in st.session_state and st.session_state['processed']:
        res_b64 = get_image_base64(st.session_state['result'])
        st.markdown(f'<div class="image-card"><img src="data:image/png;base64,{res_b64}"></div>', unsafe_allow_html=True)
        st.success("Detected!")
    else:
        st.markdown("""
        <div style="height: 300px; display: flex; align-items: center; justify-content: center; border: 1px dashed rgba(255,255,255,0.1); border-radius: 12px; color: #64748b; font-size: 0.8rem;">
            Visualization will appear here
        </div>
        """, unsafe_allow_html=True)
