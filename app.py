import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

st.set_page_config(page_title="RED: TopGun Physics", page_icon="⚛️", layout="wide")

# --- SEMNĂTURA ÎN MENIUL LATERAL (SIDEBAR) ---
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='text-align: center; color: #888; font-size: 0.85em;'>"
    "<b>RED: TopGun Physics</b><br>"
    "Proiect educațional<br>"
    "<b>Realizat de Hărlăuanu Cătălin Grigoraș</b>"
    "</div>", 
    unsafe_allow_html=True
)

st.title("⚛️ Laborator Virtual: TopGun Physics")
st.markdown("---")

col_text, col_anim = st.columns([1, 1])

with col_text:
    st.write("### 🦅 Bine ai venit, viitorule pilot!")
    st.write("Această platformă (RED) transformă fizica teoretică în experiență tactică. Aici, legile lui Newton nu sunt doar formule, ci cheia supraviețuirii într-un dogfight.")
    st.info("👈 Explorează capitolele din meniul lateral pentru a începe antrenamentul.")
    
    st.write("#### Obiectivele Platformei:")
    st.write("- **Curriculum BAC:** Mecanica de clasa a IX-a explicată vizual.")
    st.write("- **Elite AFA:** Secțiune dedicată admiterii la Academia Forțelor Aeriene.")
    st.write("- **Interactivitate:** Simulatoare matematice de înaltă precizie.")

# --- ANIMAȚIA SUPREMĂ DOGFIGHT (FOX 3) ---
with col_anim:
    st.write("#### 📡 Radar Tactic: Dogfight & Interceptare")
    placeholder = st.empty()
    
    raza = 50
    t_circle = np.linspace(0, 2*np.pi, 100)
    
    if st.button("🔴 Activează Scenariul de Luptă (Fox 3)"):
        trail_f35_x, trail_f35_y = [], []
        trail_en_x, trail_en_y = [], []
        flares_x, flares_y = [], []
        
        x_missile, y_missile = 0, 0
        
        for i in range(140):
            theta_en = i * 0.1
            theta_f35 = theta_en - 0.7 
            
            x_f35, y_f35 = raza * np.cos(theta_f35), raza * np.sin(theta_f35)
            trail_f35_x.append(x_f35); trail_f35_y.append(y_f35)
            if len(trail_f35_x) > 15: trail_f35_x.pop(0); trail_f35_y.pop(0)
            
            if i < 90:
                x_en, y_en = raza * np.cos(theta_en), raza * np.sin(theta_en)
                trail_en_x.append(x_en); trail_en_y.append(y_en)
                if len(trail_en_x) > 15: trail_en_x.pop(0); trail_en_y.pop(0)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=raza*np.cos(t_circle), y=raza*np.sin(t_circle), mode='lines', line=dict(color='rgba(255,255,255,0.05)', width=1)))
            
            fig.add_trace(go.Scatter(x=trail_f35_x, y=trail_f35_y, mode='lines', line=dict(color='rgba(0, 255, 255, 0.4)', width=4)))
            fig.add_trace(go.Scatter(x=[x_f35], y=[y_f35], mode='markers+text', text=["F-35"], textposition="top left", marker=dict(size=18, color='cyan', symbol='triangle-up', angle=np.degrees(theta_f35)+90)))
            
            if i < 90:
                fig.add_trace(go.Scatter(x=trail_en_x, y=trail_en_y, mode='lines', line=dict(color='rgba(255, 0, 0, 0.4)', width=4)))
                fig.add_trace(go.Scatter(x=[x_en], y=[y_en], mode='markers+text', text=["Inamic"], textposition="bottom right", marker=dict(size=18, color='red', symbol='triangle-up', angle=np.degrees(theta_en)+90)))
            
            if 40 <= i < 90:
                if i == 40:
                    x_missile, y_missile = x_f35, y_f35
                x_missile = x_missile + (x_en - x_missile) * 0.15 
                y_missile = y_missile + (y_en - y_missile) * 0.15
                fig.add_trace(go.Scatter(x=[x_missile], y=[y_missile], mode='markers', marker=dict(color='yellow', size=8, symbol='circle')))
            
            if 65 <= i < 90:
                if i % 3 == 0:
                    flares_x.append(x_en + np.random.uniform(-5, 5))
                    flares_y.append(y_en + np.random.uniform(-5, 5))
                fig.add_trace(go.Scatter(x=flares_x, y=flares_y, mode='markers', marker=dict(color='orange', size=6, symbol='star')))
            
            if 90 <= i < 115:
                fig.add_trace(go.Scatter(x=[x_en], y=[y_en], mode='text', text=['💥'], textfont=dict(size=55)))
            
            fig.update_layout(template="plotly_dark", xaxis=dict(range=[-75, 75], showgrid=False, zeroline=False, showticklabels=False), yaxis=dict(range=[-75, 75], showgrid=False, zeroline=False, showticklabels=False), height=450, margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
            placeholder.plotly_chart(fig, use_container_width=True)
            time.sleep(0.02)
            
        st.success("🎯 Țintă distrusă! Misiune îndeplinită, Splash One!")
