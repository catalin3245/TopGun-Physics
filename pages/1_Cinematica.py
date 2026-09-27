import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="1. Cinematica", layout="wide")
st.title("1️⃣ Cinematica Punctului Material")

st.write("### 📌 Formulele Matematice (M.R.U.V.)")
st.latex(r"v(t) = v_0 + a \cdot t")
st.latex(r"d(t) = v_0 \cdot t + \frac{a \cdot t^2}{2}")

st.write("### ⚙️ Simulator Interactiv: Spațiul de Frânare Auto")
col1, col2 = st.columns(2)
with col1:
    viteza_kmh = st.slider("Viteza inițială a vehiculului (km/h)", 30.0, 150.0, 90.0, step=10.0)
    deceleratie = st.slider("Decelerația de frânare (m/s²)", 2.0, 10.0, 6.0, step=0.5)

viteza_ms = viteza_kmh / 3.6
timp_oprire = viteza_ms / deceleratie
distanta_oprire = (viteza_ms**2) / (2 * deceleratie)

with col2:
    st.metric(label="Timpul total până la oprire", value=f"{timp_oprire:.2f} s")
    st.metric(label="Distanța totală de frânare", value=f"{distanta_oprire:.1f} m")

timp_grafic = [t * 0.1 for t in range(int(timp_oprire * 10) + 5)]
distanta_lista = [viteza_ms * t - 0.5 * deceleratie * (t**2) if t <= timp_oprire else distanta_oprire for t in timp_grafic]
viteza_lista = [viteza_ms - deceleratie * t if t <= timp_oprire else 0 for t in timp_grafic]

fig = go.Figure()
fig.add_trace(go.Scatter(x=timp_grafic, y=distanta_lista, mode='lines', name='Distanța (m)', line=dict(color='cyan', width=4)))
fig.add_trace(go.Scatter(x=timp_grafic, y=viteza_lista, mode='lines', name='Viteza (m/s)', line=dict(color='red', width=4, dash='dash')))
fig.update_layout(title="Graficul Frânării", xaxis_title="Timp (s)", template="plotly_dark")
st.plotly_chart(fig, width="stretch")