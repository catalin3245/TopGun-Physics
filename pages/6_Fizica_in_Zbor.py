import streamlit as st
import math
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Academia AFA", layout="wide")

st.title("🦅 Academia Forțelor Aeriene: Mecanica Zborului Tactic")

st.image("image_5.png", caption="F-35 Lightning II: Fizica zborului tactic", use_container_width=True)

st.write("Bine ai venit în modulul de excelență pentru viitorii piloți militari. Navighează prin tab-urile de mai jos pentru a parcurge antrenamentul teoretic și practic.")

# Am adăugat al 5-lea tab pentru Fun Facts!
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌪️ Portanța (Aero)", 
    "🚀 Viteza Mach", 
    "🎢 Forța Centrifugă (G)", 
    "🎖️ Quiz Academie", 
    "💡 Dosarul F-35 (Fun Facts)"
])

with tab1:
    st.subheader("Mecanica Fluidelor: Forța de Portanță (Lift)")
    st.write("Pentru ca o aeronavă de vânătoare să zboare, aripile sale trebuie să genereze o forță de ridicare care să depășească greutatea avionului. Aceasta depinde de densitatea aerului, viteza la pătrat și suprafața portantă.")
    st.latex(r"L = \frac{1}{2} \cdot \rho \cdot v^2 \cdot S \cdot C_L")
    
    col1, col2 = st.columns(2)
    with col1:
        altitudine_p = st.slider("Altitudine de zbor (m) ", 0, 20000, 5000, step=500, key="alt_portanta")
        viteza_kmh_p = st.slider("Viteza aeronavei (km/h)", 200, 2500, 900, step=50, key="vit_portanta")
    
    densitate_aer = 1.225 * math.exp(-0.0001 * altitudine_p)
    viteza_ms_p = viteza_kmh_p / 3.6
    portanta_kn = (0.5 * densitate_aer * (viteza_ms_p**2) * 40.0 * 0.5) / 1000
    
    with col2:
        st.metric("Densitatea Aerului", f"{densitate_aer:.3f} kg/m³")
        st.metric("Forța de Portanță Generată", f"{portanta_kn:.0f} kN")
        if portanta_kn < 150:
            st.error("⚠️ STALL! Portanță insuficientă pentru un avion de 15 tone. Crește viteza sau coboară la o altitudine cu aer mai dens!")
        else:
            st.success("🟢 Zbor stabil.")

with tab2:
    st.subheader("Termodinamica: Viteza Sunetului (Mach)")
    st.write("Bariera sunetului nu este o viteză fixă. Ea scade pe măsură ce urci în altitudine, deoarece temperatura aerului scade.")
    st.latex(r"a = 20.05 \cdot \sqrt{T}")
    
    col3, col4 = st.columns(2)
    with col3:
        altitudine_m = st.slider("Altitudine de zbor (m)", 0, 20000, 10000, step=500, key="alt_mach")
        mach_target = st.slider("Tracțiune (Numărul Mach dorit)", 0.5, 3.0, 1.2, step=0.1, key="mach_mach")
        
    temp_c = 15.0 - (0.0065 * altitudine_m)
    vit_sunet_kmh = (20.05 * math.sqrt(temp_c + 273.15)) * 3.6
    vit_reala = mach_target * vit_sunet_kmh
    
    with col4:
        st.metric("Temperatura exterioară", f"{temp_c:.1f} °C")
        st.metric("Viteza Sunetului (Mach 1) la această altitudine", f"{vit_sunet_kmh:.0f} km/h")
        st.metric(f"Viteza ta reală la Mach {mach_target}", f"{vit_reala:.0f} km/h")

with tab3:
    st.subheader("Dinamica Virajului și Factorul de Sarcină (Forța G)")
    st.write("Când aeronava se înclină pentru a vira rapid, portanța trebuie să susțină și forța centrifugă. Asta face ca greutatea resimțită de pilot să crească dramatic.")
    
    col5, col6 = st.columns(2)
    with col5:
        unghi_inclinare = st.slider("Unghiul de înclinare al aripilor (Grade °)", 0, 85, 60, step=5)
        viteza_baza_stall = st.number_input("Viteza de angajare la orizontală (km/h)", value=200, step=10)

    factor_sarcina_g = 1 / math.cos(math.radians(unghi_inclinare))
    viteza_stall_viraj = viteza_baza_stall * math.sqrt(factor_sarcina_g)

    with col6:
        st.metric(label="Factorul de Sarcină (Forța G)", value=f"{factor_sarcina_g:.2f} G")
        st.metric(label="Viteza minimă de supraviețuire (Stall Speed)", value=f"{viteza_stall_viraj:.0f} km/h")
        if factor_sarcina_g > 9:
            st.error("🩸 PERICOL G-LOC! Limita umană a fost depășită!")
            
    unghiuri = np.linspace(0, 85, 100)
    g_valori = 1 / np.cos(np.radians(unghiuri))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=unghiuri, y=g_valori, mode='lines', name='Forța G vs. Înclinare', line=dict(color='orange', width=4)))
    fig.add_trace(go.Scatter(x=[unghi_inclinare], y=[factor_sarcina_g], mode='markers', name='Avionul Tău', marker=dict(color='red', size=15)))
    fig.update_layout(title="Creșterea Forței G în funcție de înclinarea aeronavei", xaxis_title="Unghi de Înclinare (Grade)", yaxis_title="Forța G", template="plotly_dark")
    st.plotly_chart(fig) 

with tab4:
    st.subheader("🎖️ Academia Militară: Evaluare Tactică")
    st.write("Examenul final pentru admiterea la manșa aeronavelor de vânătoare. Răspunde corect la cele 5 întrebări pentru a obține gradul maxim.")
    
    if 'scor_afa' not in st.session_state:
        st.session_state.scor_afa = 0
        
    grad = "Cadet"
    if st.session_state.scor_afa == 10: grad = "Sublocotenent"
    elif st.session_state.scor_afa == 20: grad = "Locotenent"
    elif st.session_state.scor_afa == 30: grad = "Căpitan"
    elif st.session_state.scor_afa == 40: grad = "Maior"
    elif st.session_state.scor_afa == 50: grad = "Comandor (Top Gun) 🏆"
    
    st.markdown(f"#### 🎓 Grad actual: **{grad}** | 📊 Scor: {st.session_state.scor_afa}/50")
    st.markdown("---")
    
    r1 = st.radio("1. (Aerodinamică) Forța de portanță se opune direct cărei alte forțe fundamentale?", ["Selectează", "Tracțiunii (Thrust)", "Frecării (Drag)", "Greutății (Weight)"], key="q1_afa")
    r2 = st.radio("2. (Termodinamică) Pentru a depăși bariera sunetului (Mach 1) la 15.000 metri altitudine, viteza necesară în km/h este:", ["Selectează", "Mai mare decât la nivelul mării", "Mai mică decât la nivelul mării", "Identică, altitudinea nu contează"], key="q2_afa")
    r3 = st.radio("3. (Dinamica Virajului) Ce se întâmplă cu viteza de angajare (Stall speed) atunci când înclini puternic avionul într-un viraj?", ["Selectează", "Scade", "Crește periculos de mult", "Rămâne constantă"], key="q3_afa")
    r4 = st.radio("4. (Fiziologie Aerospațială) Fenomenul G-LOC (pierderea cunoștinței) apare atunci când:", ["Selectează", "Zbori prea sus fără mască de oxigen", "Sângele este împins dinspre cap spre picioare din cauza forței centrifuge pozitive", "Zbori cu viteză supersonică în linie dreaptă"], key="q4_afa")
    r5 = st.radio("5. (Mecanica Fluidelor) Ce se întâmplă cu portanța dacă densitatea aerului scade, dar păstrezi viteza constantă?", ["Selectează", "Portanța scade", "Portanța crește", "Nu este afectată"], key="q5_afa")
    
    if st.button("Finalizează Examenul AFA"):
        puncte_afa = 0
        if r1 == "Greutății (Weight)": puncte_afa += 10
        if r2 == "Mai mică decât la nivelul mării": puncte_afa += 10
        if r3 == "Crește periculos de mult": puncte_afa += 10
        if r4 == "Sângele este împins dinspre cap spre picioare din cauza forței centrifuge pozitive": puncte_afa += 10
        if r5 == "Portanța scade": puncte_afa += 10
        
        st.session_state.scor_afa = puncte_afa
        
        if puncte_afa == 50:
            st.success(f"Perfect! Ai obținut {puncte_afa}/50 puncte. Ești pregătit pentru manșă!")
        elif puncte_afa >= 30:
            st.warning(f"Admis parțial. Ai obținut {puncte_afa}/50 puncte. Mai studiază teoria!")
        else:
            st.error(f"Respins. Ai obținut {puncte_afa}/50 puncte. Trebuie să refaci antrenamentul tactic.")
            
        st.rerun()

# NOUL TAB - DOSARUL F-35
with tab5:
    st.subheader("💡 Dosarul F-35: 10 Lucruri Fascinante despre Fizica în Zbor")
    
    st.markdown("""
    1. **Amprenta radar de mărimea unei mingi de golf:** Datorită geometriei sale stealth și materialelor absorbante de unde radar, F-35 are pe ecranele inamice o semnătură radar (RCS) echivalentă cu cea a unei mingi de golf, deși cântărește peste 20 de tone!
    2. **Cască de 400.000$ cu raze X vizuale:** Casca pilotului este conectată la 6 camere infraroșu distribuite pe fuselaj. Când pilotul se uită în jos, nu vede podeaua avionului, ci vede direct *prin* avion, direct la sol!
    3. **Motorul care produce 190.000 Newtoni:** Motorul Pratt & Whitney F135 generează o forță de tracțiune incredibilă de 43.000 lbs (aprox. 190 kN), fiind cel mai puternic motor instalat vreodată pe un avion de vânătoare.
    4. **Oprirea în aer (F-35B):** Varianta B a avionului folosește "vectorizarea tracțiunii". Poate roti duza motorului cu 90 de grade în jos, anulând exact forța de greutate ($T = G$), permițându-i să stea pe loc în aer.
    5. **Boom-ul Supersonic:** La viteza maximă de Mach 1.6, avionul comprimă moleculele de aer mai repede decât se pot da acestea la o parte, creând o undă de șoc uriașă și acel sunet exploziv numit *sonic boom*.
    6. **Efectul G-Force de 9G:** În viraje de luptă, un pilot de F-35 experimentează 9G. Asta înseamnă că la o greutate normală de 80 kg, pilotul se va simți ca și cum ar cântări **720 kg**, inima luptând contra gravitației să pompeze sânge la creier.
    7. **Temperatura de fricțiune:** La viteze supersonice, frecarea cu aerul încinge fuselajul avionului la sute de grade Celsius, fizica termodinamică obligând inginerii să dezvolte un strat invizibil care să disipeze căldura.
    8. **Rachete ascunse:** Pentru a păstra forma aerodinamică perfectă și profilul stealth (frecare mică), F-35 își ține armamentul în burta avionului. Ușile se deschid, lansează racheta, și se închid în mai puțin de o secundă.
    9. **Fuziunea senzorilor (Calculatoare zburătoare):** Avionul procesează gigabytes de date pe secundă (radar, termal, electronic). Calculatorul rezolvă ecuații cinematice de interceptare în milisecunde, afișând pilotului doar soluția finală.
    10. **Acrobații imposibile:** Datorită instabilității aerodinamice intenționate (aerodinamica relaxată), F-35 ar cădea din cer în mod normal. Avionul zboară doar pentru că un computer ajustează aripile de sute de ori pe secundă pentru a-l ține drept!
    """)
    
    st.markdown("---")
    st.markdown("### 🇷🇴 Începând cu anul 2030, România va primi primele aeronave F-35 Lightning II.")
    st.success("**This is your chance. Work hard!** ✈️")