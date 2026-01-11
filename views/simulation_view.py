import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from streamlit_option_menu import option_menu
from views.components import card_metric, icon
from views.styles import COLOR_PRIMARY, COLOR_SEC, COLOR_ACCENT

# --- Dummy Data Generators (Matching DataService Schema) ---
def get_dummy_class_data():
    """Generates dummy data matching the exact schema of DataService.get_class_data"""
    data = {
        'Nama': ['Andi (Sim)', 'Budi (Sim)', 'Citra (Sim)', 'Dewi (Sim)', 'Eko (Sim)', 'Fajar (Sim)', 'Gita (Sim)', 'Hadi (Sim)'],
        'Level': [3, 5, 2, 6, 1, 4, 3, 5],
        'XP': [320, 550, 180, 700, 80, 410, 350, 520],
        'Kelancaran_Avg': [75, 88, 50, 95, 40, 78, 65, 85], 
        'Status_Hari_Ini': ['Normal', 'Lancar', 'Terbata', 'Lancar', 'Terbata', 'Lancar', 'Normal', 'Lancar'],
        'Kata_Sulit': [[], ['Eks-tra'], ['Me-nga-pa'], [], ['Ba-ca', 'Tu-lis'], [], ['Me-nyan-yi'], []],
        'Diagnosis': [
            "Perlu latihan rutin.",
            "Sangat baik.",
            "Masih terbata-bata.",
            "Luar biasa.",
            "Perlu bimbingan khusus.",
            "Konsisten.",
            "Cukup baik.",
            "Bagus sekali."
        ]
    }
    return pd.DataFrame(data)

def get_dummy_student_data():
    """Generates dummy single student data matching DataService.get_student_data"""
    return {
        'Nama': 'Budi Santoso (Simulasi)',
        'Level': 5,
        'XP': 550,
        'Kelancaran_Avg': 88,
        'Status_Hari_Ini': 'Lancar',
        'Kata_Sulit': ['Me-nye-lam'],
        'Diagnosis': "Secara umum sangat lancar, hanya ragu di kata majemuk."
    }

# ==============================================================================
# GURU VIEW REPLICA (Shadowing views/guru_view.py)
# ==============================================================================

@st.dialog("Detail Siswa (Simulasi)", width="large")
def show_sim_student_detail(student):
    # --- Profile Header ---
    st.markdown(f"""
    <div class="soft-card" style="display:flex; align-items:center; gap:20px; padding: 20px; border-left: 5px solid {COLOR_PRIMARY}; background: #F8FAFC;">
        <div style="border-radius: 50%; overflow:hidden; width:80px; height:80px; border: 3px solid {COLOR_PRIMARY}; flex-shrink: 0;">
            <img src="https://img.freepik.com/free-vector/cute-owl-sitting-tree-branch-cartoon-vector-illustration_138676-2187.jpg?w=100" width="80" style="object-fit: cover;">
        </div>
        <div style="flex-grow: 1;">
            <div style="font-size: 0.85rem; color: {COLOR_SEC}; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Siswa Kelas 1-A</div>
            <h3 style="margin:0; color:{COLOR_PRIMARY}; font-size: 1.5rem;">{student['Nama']}</h3>
            <div style="display: flex; gap: 10px; margin-top: 8px;">
                <span style="background:{COLOR_PRIMARY}; color:white; padding: 2px 10px; border-radius:12px; font-size:0.75rem; font-weight: 500;">Level {student['Level']}</span>
                <span style="background:#E2E8F0; color:{COLOR_SEC}; padding: 2px 10px; border-radius:12px; font-size:0.75rem;">Total XP: <b>{student['XP']}</b></span>
            </div>
        </div>
        <div style="text-align: right;">
             <div style="font-size: 0.75rem; color: #64748B;">Kelancaran</div>
             <div style="font-size: 1.8rem; font-weight: 700; color: {COLOR_PRIMARY};">{student['Kelancaran_Avg']}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Detail Content ---
    c_chart, c_analysis = st.columns([1.5, 1])
    
    with c_chart:
        st.markdown(f"<h6 style='color:{COLOR_SEC}; margin-top: 10px;'>{icon('bi-graph-up', color=COLOR_PRIMARY)} Progress Mingguan</h6>", unsafe_allow_html=True)
        trend_data = pd.DataFrame({
            'Hari': ['Sen', 'Sel', 'Rab', 'Kam'], 
            'Skor': [random.randint(60,95) for _ in range(4)]
        })
        st.area_chart(trend_data.set_index('Hari'), color=COLOR_PRIMARY, height=220)

    with c_analysis:
        st.markdown(f"<h6 style='color:{COLOR_SEC}; margin-top: 10px;'>{icon('bi-cpu', color=COLOR_PRIMARY)} Analisis AI</h6>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="suggestion-box" style="font-size: 0.9rem; margin-bottom: 15px; color: {COLOR_SEC};">
            <b style="color: {COLOR_PRIMARY};">Feedback:</b><br>
            {student['Diagnosis']}
        </div>
        """, unsafe_allow_html=True)
        
        if len(student['Kata_Sulit']) > 0:
            st.markdown(f"<div style='font-size:0.85rem; font-weight:600; color:#9A3412; margin-bottom: 5px;'>Fokus Perbaikan ({len(student['Kata_Sulit'])} kata):</div>", unsafe_allow_html=True)
            html_tags = "".join([f"<span class='word-tag' style='font-size: 0.8rem;'>{w}</span>" for w in student['Kata_Sulit']])
            st.markdown(f"<div style='line-height: 1.6;'>{html_tags}</div>", unsafe_allow_html=True)
        else:
             st.markdown(f"""
            <div style="background-color:#F0FDFA; border:1px solid {COLOR_PRIMARY}; padding: 10px; border-radius: 8px; text-align:center; font-size: 0.85rem; color: {COLOR_PRIMARY};">
                {icon('bi-check-circle-fill')} Tidak ada kata sulit.
            </div>
            """, unsafe_allow_html=True)

def render_sim_guru_header():
    st.markdown(f"""
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: -15px;">
{icon('bi-joystick', size="1.8rem", color=COLOR_PRIMARY)}
<h2 style="margin: 0; padding: 0; color: {COLOR_PRIMARY};">Dashboard Kelas (Simulasi)</h2>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<p style='color:#64748B; margin-left: 5px;'>Mode Simulasi: Data yang ditampilkan adalah dummy.</p>", unsafe_allow_html=True)
    st.divider()

def render_sim_guru_metrics(df):
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(card_metric("Total Siswa", len(df), icon_name="bi-people-fill"), unsafe_allow_html=True)
    with k2: st.markdown(card_metric("Rata-rata Kelas", f"{df['Kelancaran_Avg'].mean():.0f}%"), unsafe_allow_html=True)
    with k3: 
        risk_count = len(df[df['Kelancaran_Avg'] < 50])
        st.markdown(card_metric("Perlu Bantuan", f"{risk_count} Siswa", icon_name="bi-exclamation-circle-fill"), unsafe_allow_html=True)
    with k4: st.markdown(card_metric("Top XP", df['XP'].max(), icon_name="bi-trophy-fill"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

def render_sim_guru_table(df):
    st.markdown(f"""
<h5 style="display: flex; align-items: center; gap: 8px;">
{icon('bi-table', color=COLOR_SEC)} Daftar Siswa (Dummy)
</h5>
""", unsafe_allow_html=True)
    
    event = st.dataframe(
        df,
        column_config={
            "Nama": st.column_config.TextColumn("Nama Lengkap", width="medium"),
            "Kelancaran_Avg": st.column_config.ProgressColumn("Tingkat Kelancaran", format="%d%%", min_value=0, max_value=100),
            "Level": st.column_config.NumberColumn("Lvl", format="%d"),
            "Status_Hari_Ini": st.column_config.TextColumn("Status"),
            "XP": st.column_config.NumberColumn("XP", format="%d XP"),
            "Kata_Sulit": None, 
            "Diagnosis": None 
        },
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row"
    )

    if len(event.selection.rows) > 0:
        show_sim_student_detail(df.iloc[event.selection.rows[0]])

def render_sim_guru():
    render_sim_guru_header()
    df = get_dummy_class_data()
    render_sim_guru_metrics(df)
    render_sim_guru_table(df)

# ==============================================================================
# ORTU VIEW REPLICA (Shadowing views/ortu_view.py)
# ==============================================================================

def render_sim_ortu_header(child_data):
    st.markdown(f"""
    <div class="soft-card" style="border-left: 5px solid {COLOR_PRIMARY};">
        <div style="display:flex; align-items:center; gap:20px;">
            <img src="https://img.freepik.com/free-vector/wise-owl-with-graduation-cap-diploma_138676-3046.jpg?w=100" width="80" style="border-radius:12px;">
            <div>
                <h2 style="margin:0; color:{COLOR_PRIMARY}">{child_data['Nama']}</h2>
                <p style="margin:0; color:{COLOR_SEC}; font-size:0.95rem;">
                    {icon('bi-star-fill', color='#F59E0B')} Level {child_data['Level']} &nbsp;|&nbsp; ID: SIMULASI-001
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sim_ortu_report(child_data):
    st.markdown("<br>", unsafe_allow_html=True)
    col_stat, col_detail = st.columns([1, 2])
    
    with col_stat:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding: 40px 20px;">
            <div style="font-size:0.9rem; color:#64748B; text-transform:uppercase; letter-spacing:1px;">Skor Kelancaran</div>
            <div style="font-size:3.5rem; font-weight:700; color:{COLOR_PRIMARY}; line-height:1.2;">
                {child_data['Kelancaran_Avg']}<span style="font-size:1.5rem">%</span>
            </div>
            <div style="margin-top:10px; font-size:0.85rem; background:#DCFCE7; color:#166534; display:inline-block; padding:4px 12px; border-radius:20px;">
                {icon('bi-graph-up-arrow')} Meningkat dari kemarin
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_detail:
        if len(child_data['Kata_Sulit']) > 0:
            st.markdown(f"""
            <div class="alert-box">
                <h5 style="margin:0; font-family:'Poppins';">{icon('bi-exclamation-triangle-fill')} Perlu Latihan Mandiri</h5>
                <p style="margin-top:5px; font-size:0.9rem; color:#9A3412;">
                    Anak Anda mengalami kesulitan mengeja kata-kata berikut hari ini:
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            tags = "".join([f"<span class='word-tag'>{w}</span>" for w in child_data['Kata_Sulit']])
            st.markdown(f"<div style='margin:15px 0;'>{tags}</div>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="suggestion-box">
                <b>{icon('bi-lightbulb', color=COLOR_PRIMARY)} Saran NARA AI:</b><br>
                <span style="font-size:0.95rem; color:{COLOR_SEC}">{child_data['Diagnosis']}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="soft-card" style="background-color:#F0FDFA; border:1px solid {COLOR_PRIMARY}; text-align:center;">
                <h4 style="color:{COLOR_PRIMARY};">{icon('bi-award-fill')} Luar Biasa!</h4>
                <p>Tidak ada kata sulit yang terdeteksi hari ini. Semua bacaan lancar.</p>
            </div>
            """, unsafe_allow_html=True)

def render_sim_ortu_monitoring():
    st.markdown("<br>", unsafe_allow_html=True)
    c_btn, c_info = st.columns([1, 4])
    
    # Use local state for simulation monitoring to avoid conflicting with global monitoring state
    if 'sim_monitoring_active' not in st.session_state:
        st.session_state.sim_monitoring_active = False

    with c_btn:
        active = st.session_state.sim_monitoring_active
        if not active:
            if st.button("Mulai Sesi (Sim)", type="primary", use_container_width=True):
                st.session_state.sim_monitoring_active = True
                st.rerun()
        else:
            if st.button("Stop Sesi (Sim)", type="secondary", use_container_width=True):
                st.session_state.sim_monitoring_active = False
                st.rerun()
    
    with c_info:
        active = st.session_state.sim_monitoring_active
        if active:
            st.markdown(f"<div style='padding:8px; color:{COLOR_PRIMARY}; font-weight:600;'>{icon('bi-wifi', class_name='pulse-icon')} Device Connected (SIM-01)</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='padding:8px; color:#94A3B8;'>{icon('bi-wifi-off')} Device Disconnected</div>", unsafe_allow_html=True)

    if st.session_state.sim_monitoring_active:
        chart_place = st.empty()
        st.caption("Real-time Speech-to-Text Stream (Simulated):")
        text_place = st.empty()
        
        sample_txt = "Ini adalah contoh teks yang sedang dibaca siswa dalam mode simulasi."
        words = sample_txt.split()
        current_words = []
        
        for i, w in enumerate(words):
            if not st.session_state.sim_monitoring_active: break
            chart_data = pd.DataFrame(np.random.uniform(0, 100, size=(1, 30))).T
            chart_place.bar_chart(chart_data, height=40, color=COLOR_PRIMARY)
            current_words.append(w)
            display_html = " ".join([f"<span class='highlight-active'>{word}</span>" if idx == i else word for idx, word in enumerate(current_words)])
            
            text_place.markdown(f"""
            <div class="live-terminal">
                {icon('bi-mic-fill', color=COLOR_ACCENT)} Listening...<br><br>
                {display_html} <span style="animation: blink 1s infinite;">_</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.5)
        
        text_place.markdown(f"""
        <div class="live-terminal" style="border-left-color: #10B981;">
            {icon('bi-check-circle-fill', color='#10B981')} Session Completed.<br><br>
            {sample_txt}
        </div>
        """, unsafe_allow_html=True)
        st.session_state.sim_monitoring_active = False
        if st.button("Reset Monitor"): st.rerun()
    else:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding:60px; border: 2px dashed #CBD5E1; background-color:#F8FAFC;">
            {icon('bi-headset', size="3rem", color="#94A3B8")}
            <h5 style="color:#64748B; margin-top:15px;">Monitoring Siap</h5>
            <p style="font-size:0.9rem; color:#94A3B8;">Tekan tombol 'Mulai Sesi' untuk menghubungkan ke audio stream.</p>
        </div>
        """, unsafe_allow_html=True)

def render_sim_ortu():
    child_data = get_dummy_student_data()

    render_sim_ortu_header(child_data)

    selected_tab = option_menu(
        menu_title=None, 
        options=["Laporan Harian", "Live Monitoring"], 
        icons=["journal-text", "mic"], 
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": COLOR_SEC, "font-size": "14px"}, 
            "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px 10px 0px 0px", "border-radius": "8px", "background-color": "white", "border": "1px solid #e2e8f0", "color": COLOR_SEC},
            "nav-link-selected": {"background-color": COLOR_PRIMARY, "color": "white", "border": f"1px solid {COLOR_PRIMARY}"},
        }
    )

    if selected_tab == "Laporan Harian":
        render_sim_ortu_report(child_data)
    elif selected_tab == "Live Monitoring":
        render_sim_ortu_monitoring()

# ==============================================================================
# MAIN VIEW CONTROLLER
# ==============================================================================

def view_simulation():
    # Only show role selection for simulation main page
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="background-color: #F1F5F9; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; color: #64748B; font-weight: 500;">
            {icon('bi-info-circle')} Mode Simulasi
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    sim_role = option_menu(
        menu_title=None, 
        options=["Simulasi Guru", "Simulasi Orang Tua"], 
        icons=["person-video3", "house-heart"], 
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent", "margin-bottom": "20px"},
            "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px 5px", "border-radius": "8px"},
            "nav-link-selected": {"background-color": COLOR_ACCENT, "color": "white"},
        }
    )

    if sim_role == "Simulasi Guru":
        render_sim_guru()
    else:
        render_sim_ortu()
