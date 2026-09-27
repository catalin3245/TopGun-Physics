import streamlit as st
import math
import plotly.graph_objects as go

st.set_page_config(page_title="Simulator Supersonic", layout="wide")
st.title("🚀 Aplicație Avansată: Mecanica Fluidelor (Zbor)")

col1, col2 = st.columns(2)
with col1:
    altitudine = st.slider("Altitudine de zbor (metri)", 0, 20000, 10000, step=500)
    mach = st.slider("Tracțiune Motor (Mach)", 0.0, 3.0, 1.2, step=0.1)
with col2:
    temperatura_c = 15.0 - (0.0065 * altitudine)
    viteza_sunetului_ms = 20.05 * math.sqrt(temperatura_c + 273.15)
    viteza_avion_kmh = mach * viteza_sunetului_ms * 3.6
    st.metric(label="Temperatura aerului", value=f"{temperatura_c:.1f} °C")
    st.metric(label="Viteza reală a avionului", value=f"{viteza_avion_kmh:.0f} km/h")

st.markdown("---")
st.subheader("📡 Radar Tactic: Interceptare Țintă Frontală")
col3, col4 = st.columns(2)
with col3:
    distanta_inamic = st.number_input("Distanța până la țintă (km)", value=50.0, step=5.0)
with col4:
    viteza_inamic_kmh = st.number_input("Viteza țintei (km/h)", value=900.0, step=50.0)

viteza_apropiere = viteza_avion_kmh + viteza_inamic_kmh
if viteza_apropiere > 0:
    timp_interceptare_sec = (distanta_inamic / viteza_apropiere) * 3600
    st.warning(f"⚠️ IMPACT ESTIMAT ÎN: **{timp_interceptare_sec:.1f} secunde**!")