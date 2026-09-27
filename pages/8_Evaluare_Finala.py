import streamlit as st

st.set_page_config(page_title="Evaluare RED", layout="wide")
st.title("🎓 Evaluare Finală: Fizică Mecanică")
st.write("Testează-ți cunoștințele dobândite. La finalul fiecărui test, vei primi punctajul și explicațiile detaliate pentru fiecare întrebare.")

st.markdown("---")

# Meniul de selecție a testelor
test_ales = st.selectbox("📚 Selectează Modulul de Evaluare:", [
    "Test 1: Concepte Fundamentale (Baza)", 
    "Test 2: Cinematica", 
    "Test 3: Dinamica", 
    "Test 4: Energia și Lucrul Mecanic", 
    "Test 5: Simulări complexe (Examen)"
])

st.markdown("---")

if test_ales == "Test 1: Concepte Fundamentale (Baza)":
    st.subheader("📝 Test 1: Baza Mecanicii Newtoniene")
    
    # Aici este "Motorul". O listă în care punem Întrebarea, Opțiunile, Răspunsul corect și Explicația.
    intrebari_test_1 = [
        {
            "q": "1. Care este unitatea de măsură în Sistemul Internațional (S.I.) pentru accelerație?",
            "opt": ["Selectează", "m/s", "m/s²", "Newton", "Joule"],
            "ans": "m/s²",
            "exp": "Accelerația reprezintă variația vitezei în unitatea de timp. Cum viteza se măsoară în m/s, împărțind la încă o secundă obținem m/s²."
        },
        {
            "q": "2. Principiul I al mecanicii (Principiul Inerției) afirmă că un corp își păstrează starea de repaus sau de mișcare rectilinie uniformă atâta timp cât:",
            "opt": ["Selectează", "Viteza sa este zero", "Forța rezultantă ce acționează asupra sa este zero", "Acțiunea este egală cu reacțiunea"],
            "ans": "Forța rezultantă ce acționează asupra sa este zero",
            "exp": "Dacă nicio forță netă nu intervine, inerția dictează ca un corp să nu își schimbe starea cinematică (rămâne pe loc sau merge constant)."
        },
        {
            "q": "3. Formula greutății (G) unui corp aflat pe suprafața Pământului este:",
            "opt": ["Selectează", "G = m * v", "G = m * a", "G = m * g"],
            "ans": "G = m * g",
            "exp": "Greutatea este forța cu care Pământul atrage un corp. Masa (m) se înmulțește cu accelerația gravitațională (g ≈ 9.81 m/s²)."
        },
        {
            "q": "4. Cum definim Forța de Frecare la alunecare?",
            "opt": ["Selectează", "Ff = μ * N", "Ff = m * g * h", "Ff = m * v² / 2"],
            "ans": "Ff = μ * N",
            "exp": "Forța de frecare depinde de coeficientul de frecare (μ) specific suprafețelor aflate în contact și de forța normală de apăsare (N)."
        },
        {
            "q": "5. Ce afirmă Principiul al III-lea al mecanicii (Acțiune și Reacțiune)?",
            "opt": ["Selectează", "Orice acțiune generează o reacțiune egală în modul și opusă ca sens", "Orice forță produce accelerație", "Masa atrage altă masă"],
            "ans": "Orice acțiune generează o reacțiune egală în modul și opusă ca sens",
            "exp": "Dacă apeși pe un perete cu 10N (Acțiune), peretele apasă înapoi pe mâna ta cu exact 10N, dar în sens invers (Reacțiune)."
        }
        # Pentru a adăuga întrebările 6-10, pur și simplu mai pui o virgulă mai sus și copiezi structura de mai sus!
    ]
    
    # Partea care afișează automat întrebările din lista de mai sus
    raspunsuri_utilizator = []
    for i, intrebare in enumerate(intrebari_test_1):
        rasp = st.radio(intrebare["q"], intrebare["opt"], key=f"t1_q{i}")
        raspunsuri_utilizator.append(rasp)
        st.write("") # Un spațiu gol pentru design
        
    # Butonul de trimitere și sistemul inteligent de explicații
    if st.button("Evaluează Testul 1"):
        puncte = 0
        st.markdown("### 📊 Rezultate și Explicații")
        
        for i, intrebare in enumerate(intrebari_test_1):
            if raspunsuri_utilizator[i] == "Selectează":
                st.warning(f"**Întrebarea {i+1}:** Nu ai răspuns.")
            elif raspunsuri_utilizator[i] == intrebare["ans"]:
                puncte += 10
                st.success(f"**Întrebarea {i+1}: Răspuns Corect!** \n\n📖 *Explicație:* {intrebare['exp']}")
            else:
                st.error(f"**Întrebarea {i+1}: Răspuns Greșit.** (Ai ales: {raspunsuri_utilizator[i]}) \n\n✅ Răspunsul corect era: **{intrebare['ans']}**. \n\n📖 *Explicație:* {intrebare['exp']}")
                
        scor_maxim = len(intrebari_test_1) * 10
        st.markdown("---")
        st.metric("🏆 Scor Final Test 1", f"{puncte} / {scor_maxim} puncte")

elif test_ales == "Test 2: Cinematica":
    st.info("🚧 Acest test este în curs de dezvoltare. Structura este pregătită pentru a adăuga întrebările specifice cinematicii.")
    
elif test_ales == "Test 3: Dinamica":
    st.info("🚧 Acest test este în curs de dezvoltare.")

elif test_ales == "Test 4: Energia și Lucrul Mecanic":
    st.info("🚧 Acest test este în curs de dezvoltare.")

elif test_ales == "Test 5: Simulări complexe (Examen)":
    st.info("🚧 Acest test este în curs de dezvoltare.")