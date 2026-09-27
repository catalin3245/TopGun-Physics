import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="2. Dinamica", layout="wide")
st.title("2️⃣ Dinamica și Principiile lui Newton")

st.write("### 📌 Formulele Matematice")
st.latex(r"\vec{F}_{rezultantă} = m \cdot \vec{a}")
st.latex(r"F_{frecare} = \mu \cdot m \cdot g")

st.write("### ⚙️ Simulator Interactiv: Echilibrul Forțelor")
col1, col2 = st.columns(2)
with col1:
    masa = st.slider("Masa corpului (kg)", 10.0, 500.0, 100.0, step=10.0)
    coef_frecare = st.slider("Coeficientul de frecare (μ)", 0.1, 1.0, 0.4, step=0.05)
    forta_aplicata = st.slider("Forța de Tracțiune aplicată (N)", 0.0, 3000.0, 500.0, step=50.0)

forta_frecare_max = coef_frecare * masa * 9.81
forta_rezultanta = max(0, forta_aplicata - forta_frecare_max)
acceleratia = forta_rezultanta / masa if forta_rezultanta > 0 else 0

with col2:
    st.metric(label="Forța de Frecare (Opoziție)", value=f"{forta_frecare_max:.1f} N")
    st.metric(label="Forța Rezultantă", value=f"{forta_rezultanta:.1f} N")
    st.metric(label="Accelerația indusă", value=f"{acceleratia:.2f} m/s²")

fig = go.Figure(data=[
    go.Bar(name='Tracțiune', x=['Comparație Forțe'], y=[forta_aplicata], marker_color='cyan'),
    go.Bar(name='Frecare', x=['Comparație Forțe'], y=[forta_frecare_max], marker_color='red')
])
fig.update_layout(barmode='group', title="Tracțiune vs. Frecare", template="plotly_dark")
st.plotly_chart(fig, width="stretch")