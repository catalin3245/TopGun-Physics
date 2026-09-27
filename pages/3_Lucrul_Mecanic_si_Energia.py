import streamlit as st
import plotly.graph_objects as go
import math

st.set_page_config(page_title="3. Energia", layout="wide")
st.title("3️⃣ Energia și Lucrul Mecanic")

st.write("### 📌 Formulele Matematice (Conservarea Energiei)")
st.latex(r"E_p = m \cdot g \cdot h \quad \text{și} \quad E_c = \frac{m \cdot v^2}{2}")

st.write("### ⚙️ Simulator Interactiv: Căderea Liberă")
col1, col2 = st.columns(2)
with col1:
    masa = st.slider("Masa corpului (kg)", 1.0, 100.0, 10.0)
    inaltime_initiala = st.slider("Înălțimea de lansare (m)", 10.0, 500.0, 100.0)

g = 9.81
timp_cadere = math.sqrt((2 * inaltime_initiala) / g)

with col2:
    st.metric(label="Energia Mecanică Totală (Constantă)", value=f"{masa * g * inaltime_initiala:.0f} Joules")
    st.metric(label="Timpul până la impact", value=f"{timp_cadere:.2f} secunde")

timp_grafic = [t * 0.1 for t in range(int(timp_cadere * 10) + 1)]
ep_lista = [masa * g * max(0, inaltime_initiala - 0.5 * g * (t**2)) for t in timp_grafic]
ec_lista = [0.5 * masa * ((g * t)**2) for t in timp_grafic]

fig = go.Figure()
fig.add_trace(go.Scatter(x=timp_grafic, y=ep_lista, mode='lines', name='Energie Potențială', line=dict(color='cyan', width=4)))
fig.add_trace(go.Scatter(x=timp_grafic, y=ec_lista, mode='lines', name='Energie Cinetică', line=dict(color='red', width=4)))
fig.update_layout(title="Transformarea Energiei", xaxis_title="Timp (s)", template="plotly_dark")
st.plotly_chart(fig, width="stretch")