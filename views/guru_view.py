import streamlit as st
import pandas as pd
import random
from views.styles import get_current_theme
from views.components import icon, card_metric
from models.data_service import DataService

@st.dialog("Detail Siswa", width="large")
def show_student_detail(student):
    t = get_current_theme()
    # --- Profile Header ---
    st.markdown(f"""
    <div class="soft-card" style="display:flex; align-items:center; gap:20px; padding: 20px; border-left: 5px solid {t['primary']}; background: {t['card_bg']};">
        <div style="border-radius: 50%; overflow:hidden; width:80px; height:80px; border: 3px solid {t['primary']}; flex-shrink: 0;">
            <img src="https://img.freepik.com/free-vector/cute-owl-sitting-tree-branch-cartoon-vector-illustration_138676-2187.jpg?w=100" width="80" style="object-fit: cover;">
        </div>
        <div style="flex-grow: 1;">
            <div style="font-size: 0.85rem; color: {t['secondary']}; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Siswa Kelas 1-A</div>
            <h3 style="margin:0; color:{t['primary']}; font-size: 1.5rem;">{student['Nama']}</h3>
            <div style="display: flex; gap: 10px; margin-top: 8px;">
                <span style="background:{t['primary']}; color:white; padding: 2px 10px; border-radius:12px; font-size:0.75rem; font-weight: 500;">Level {student['Level']}</span>
                <span style="background:{t['secondary']}20; color:{t['secondary']}; padding: 2px 10px; border-radius:12px; font-size:0.75rem;">Total XP: <b>{student['XP']}</b></span>
            </div>
        </div>
        <div style="text-align: right;">
             <div style="font-size: 0.75rem; color: {t['secondary']}; opacity: 0.8;">Kelancaran</div>
             <div style="font-size: 1.8rem; font-weight: 700; color: {t['primary']};">{student['Kelancaran_Avg']}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Detail Content ---
    c_chart, c_analysis = st.columns([1.5, 1])
    
    with c_chart:
        st.markdown(f"<h6 style='color:{t['secondary']}; margin-top: 10px;'>{icon('bi-graph-up', color=t['primary'])} Progress Mingguan</h6>", unsafe_allow_html=True)
        trend_data = pd.DataFrame({
            'Hari': ['Sen', 'Sel', 'Rab', 'Kam'], 
            'Skor': [random.randint(60,95) for _ in range(4)]
        })
        st.area_chart(trend_data.set_index('Hari'), color=t['primary'], height=220)

    with c_analysis:
        st.markdown(f"<h6 style='color:{t['secondary']}; margin-top: 10px;'>{icon('bi-cpu', color=t['primary'])} Analisis AI</h6>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="suggestion-box" style="font-size: 0.9rem; margin-bottom: 15px; color: {t['secondary']};">
            <b style="color: {t['primary']};">Feedback:</b><br>
            {student['Diagnosis']}
        </div>
        """, unsafe_allow_html=True)
        
        if len(student['Kata_Sulit']) > 0:
            st.markdown(f"<div style='font-size:0.85rem; font-weight:600; color:{t['accent']}; margin-bottom: 5px;'>Fokus Perbaikan ({len(student['Kata_Sulit'])} kata):</div>", unsafe_allow_html=True)
            html_tags = "".join([f"<span class='word-tag' style='font-size: 0.8rem;'>{w}</span>" for w in student['Kata_Sulit']])
            st.markdown(f"<div style='line-height: 1.6;'>{html_tags}</div>", unsafe_allow_html=True)
        else:
             st.markdown(f"""
            <div style="background-color:{t['background']}; border:1px solid {t['primary']}; padding: 10px; border-radius: 8px; text-align:center; font-size: 0.85rem; color: {t['primary']};">
                {icon('bi-check-circle-fill')} Tidak ada kata sulit.
            </div>
            """, unsafe_allow_html=True)

def render_guru_header():
    t = get_current_theme()
    st.markdown(f"""
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: -15px;">
{icon('bi-grid-1x2-fill', size="1.8rem", color=t['primary'])}
<h2 style="margin: 0; padding: 0; color: {t['primary']};">Dashboard Kelas 1-A</h2>
</div>
""", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color:{t['secondary']}; margin-left: 5px; opacity: 0.8;'>Ringkasan performa literasi siswa hari ini.</p>", unsafe_allow_html=True)
    st.divider()

def render_guru_metrics(df):
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(card_metric("Total Siswa", len(df), icon_name="bi-people-fill"), unsafe_allow_html=True)
    with k2: st.markdown(card_metric("Rata-rata Kelas", f"{df['Kelancaran_Avg'].mean():.0f}%"), unsafe_allow_html=True)
    with k3: 
        risk_count = len(df[df['Kelancaran_Avg'] < 50])
        st.markdown(card_metric("Perlu Bantuan", f"{risk_count} Siswa", icon_name="bi-exclamation-circle-fill"), unsafe_allow_html=True)
    with k4: st.markdown(card_metric("Top XP", df['XP'].max(), icon_name="bi-trophy-fill"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

def render_guru_table(df):
    t = get_current_theme()
    st.markdown(f"""
<h5 style="display: flex; align-items: center; gap: 8px;">
{icon('bi-table', color=t['secondary'])} Daftar Siswa
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
        show_student_detail(df.iloc[event.selection.rows[0]])

def view_guru():
    render_guru_header()
    df = DataService.get_class_data()
    render_guru_metrics(df)
    render_guru_table(df)
