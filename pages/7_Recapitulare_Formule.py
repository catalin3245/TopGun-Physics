import streamlit as st

st.set_page_config(page_title="Recapitulare Formule", layout="wide")

st.title("📚 Recapitulare: Formulele Fundamentale")
st.write("Înainte de a intra în centrul de testare, treci în revistă toate formulele de fizică mecanică de care vei avea nevoie.")

# Folosim funcția expander pentru a nu aglomera ecranul vizual
with st.expander("1️⃣ Cinematica Punctului Material", expanded=True):
    st.latex(r"v = \frac{d}{t} \quad \text{(Viteza medie / M.R.U.)}")
    st.latex(r"v(t) = v_0 + a \cdot t \quad \text{(Legea vitezei în M.R.U.V.)}")
    st.latex(r"d(t) = v_0 \cdot t + \frac{a \cdot t^2}{2} \quad \text{(Legea mișcării în M.R.U.V.)}")
    st.latex(r"v^2 = v_0^2 + 2 \cdot a \cdot d \quad \text{(Ecuația lui Galilei)}")

with st.expander("2️⃣ Dinamica și Principiile lui Newton"):
    st.latex(r"F = m \cdot a \quad \text{(Principiul II fundamental)}")
    st.latex(r"G = m \cdot g \quad \text{(Greutatea, cu } g \approx 9.81 \, m/s^2 \text{)}")
    st.latex(r"F_f = \mu \cdot N \quad \text{(Forța de frecare la alunecare)}")
    st.latex(r"F_e = k \cdot \Delta l \quad \text{(Forța elastică / Legea lui Hooke)}")

with st.expander("3️⃣ Lucrul Mecanic, Puterea și Energia"):
    st.latex(r"L = F \cdot d \cdot \cos(\alpha) \quad \text{(Lucrul Mecanic)}")
    st.latex(r"P = \frac{L}{t} = F \cdot v \quad \text{(Puterea Mecanică)}")
    st.latex(r"E_c = \frac{m \cdot v^2}{2} \quad \text{(Energia Cinetică)}")
    st.latex(r"E_p = m \cdot g \cdot h \quad \text{(Energia Potențială Gravitațională)}")
    st.latex(r"E_{total} = E_c + E_p = \text{constant} \quad \text{(Legea Conservării Energiei)}")

with st.expander("4️⃣ Impulsul Mecanic și Ciocnirile"):
    st.latex(r"p = m \cdot v \quad \text{(Impulsul Mecanic)}")
    st.latex(r"\Delta p = F \cdot \Delta t \quad \text{(Teorema variației impulsului)}")
    st.latex(r"m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2' \quad \text{(Conservarea impulsului la ciocniri)}")

with st.expander("🦅 Dosarul AFA: Zbor Tactic (Mecanica Fluidelor)"):
    st.latex(r"L = \frac{1}{2} \cdot \rho \cdot v^2 \cdot S \cdot C_L \quad \text{(Forța de Portanță)}")
    st.latex(r"a = 20.05 \cdot \sqrt{T} \quad \text{(Viteza Sunetului)}")
    st.latex(r"n = \frac{1}{\cos(\theta)} \quad \text{(Factorul de sarcină / Forța G)}")
    st.latex(r"v_{stall} = v_{s0} \cdot \sqrt{n} \quad \text{(Viteza de angajare în viraj)}")

st.markdown("---")
st.success("✅ Acum ești complet pregătit! Accesează **8 Evaluare Finala** din meniul lateral pentru a-ți testa cunoștințele.")