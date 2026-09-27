import streamlit as st
import plotly.graph_objects as go
import time

st.set_page_config(page_title="4. Ciocniri", layout="wide")
st.title("4️⃣ Impulsul Mecanic și Ciocnirile Elastice")

st.write("### 🎬 Simulator Animat: Ciocnire Frontală")
col1, col2 = st.columns(2)
with col1:
    m1 = st.slider("Masa Bila Albastră (kg)", 1, 10, 5)
    v1 = st.slider("Viteza Bila Albastră (m/s) ->", 1, 20, 10)
with col2:
    m2 = st.slider("Masa Bila Roșie (kg)", 1, 10, 5)
    v2 = st.slider("<- Viteza Bila Roșie (m/s)", -20, -1, -10)

v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

st.write(f"**După impact:** Bila albastră = {v1_final:.2f} m/s | Bila roșie = {v2_final:.2f} m/s.")

if st.button("▶️ Rulează Animația Ciocnirii"):
    grafic_animat = st.empty() 
    x1, x2 = -50.0, 50.0 
    
    for i in range(40):
        if x1 < x2: 
            x1 += v1
            x2 += v2
        else: 
            x1 += v1_final
            x2 += v2_final
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[x1], y=[0], mode='markers', marker=dict(size=40, color='cyan'), name='Bila 1'))
        fig.add_trace(go.Scatter(x=[x2], y=[0], mode='markers', marker=dict(size=40, color='red'), name='Bila 2'))
        fig.update_layout(xaxis=dict(range=[-100, 100]), yaxis=dict(range=[-2, 2], showticklabels=False),
                          title="Animație Ciocnire", template="plotly_dark", height=300)
        grafic_animat.plotly_chart(fig, width="stretch", key=f"cadru_{i}")
        time.sleep(0.05)