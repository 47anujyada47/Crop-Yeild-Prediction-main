import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("crop_yield_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

# ---------- UI (no functional changes) ----------
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(135deg, #0b3d2e 0%, #061827 50%, #0b3d2e 100%); color: #ffffff; }
    .header { font-size: 2.2rem; font-weight: 800; letter-spacing: .4px; }
    .card { background: rgba(255,255,255,0.08); padding: 1rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.15); }
    .metric { font-size: 1.05rem; opacity: 0.95; }
    div[data-testid="stNumberInput"] > div { background: rgba(255,255,255,0.06); border-radius: 12px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="header">🌾 Crop Yield Prediction</div>', unsafe_allow_html=True)
st.write("Predict crop yield using environmental and agricultural factors.")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚙️ Enter Input Features")
    area = st.number_input("Area (hectares)", min_value=0.0, step=1.0)
    annual_rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0, step=0.1)
    fertilizer = st.number_input("Fertilizer Usage", min_value=0.0, step=0.1)
    pesticide = st.number_input("Pesticide Usage", min_value=0.0, step=0.1)

    c1, c2 = st.columns([2, 1])
    with c2:
        predict_clicked = st.button("✨ Predict Yield", use_container_width=True)
    with c1:
        st.caption("Model uses the features: Area, Annual Rainfall, Fertilizer, Pesticide.")

    st.markdown('</div>', unsafe_allow_html=True)

if predict_clicked:
    input_data = np.array([[area, annual_rainfall, fertilizer, pesticide]])
    prediction = model.predict(input_data)

    st.success(f"🌱 Predicted Crop Yield: {prediction[0]:.2f}")
    st.markdown(
        f"<div class='metric'>Tip: Try increasing rainfall or fertilizer to see how the prediction changes.</div>",
        unsafe_allow_html=True,
    )


