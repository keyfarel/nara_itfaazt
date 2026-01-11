import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from streamlit_option_menu import option_menu
from views.styles import get_current_theme, THEMES
from views.components import icon
from models.data_service import DataService

def render_ortu_header(child_data):
    t = get_current_theme()
    st.markdown(f"""
    <div class="soft-card" style="border-left: 5px solid {t['primary']}; background-color: {t['card_bg']};">
        <div style="display:flex; align-items:center; gap:20px;">
            <img src="https://img.freepik.com/free-vector/wise-owl-with-graduation-cap-diploma_138676-3046.jpg?w=100" width="80" style="border-radius:12px;">
            <div>
                <h2 style="margin:0; color:{t['primary']}">{child_data['Nama']}</h2>
                <p style="margin:0; color:{t['secondary']}; font-size:0.95rem;">
                    {icon('bi-star-fill', color='#F59E0B')} Level {child_data['Level']} &nbsp;|&nbsp; ID: {random.randint(10000,99999)}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_ortu_report(child_data):
    t = get_current_theme()
    st.markdown("<br>", unsafe_allow_html=True)
    col_stat, col_detail = st.columns([1, 2])
    
    with col_stat:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding: 40px 20px; background-color: {t['card_bg']};">
            <div style="font-size:0.9rem; color:{t['secondary']}; text-transform:uppercase; letter-spacing:1px; opacity:0.8;">Skor Kelancaran</div>
            <div style="font-size:3.5rem; font-weight:700; color:{t['primary']}; line-height:1.2;">
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
                <p style="margin-top:5px; font-size:0.9rem; color:{t['text']}; opacity: 0.9;">
                    Anak Anda mengalami kesulitan mengeja kata-kata berikut hari ini:
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            tags = "".join([f"<span class='word-tag'>{w}</span>" for w in child_data['Kata_Sulit']])
            st.markdown(f"<div style='margin:15px 0;'>{tags}</div>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="suggestion-box">
                <b>{icon('bi-lightbulb', color=t['primary'])} Saran NARA AI:</b><br>
                <span style="font-size:0.95rem; color:{t['secondary']}">{child_data['Diagnosis']}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="soft-card" style="background-color:{t['background']}; border:1px solid {t['primary']}; text-align:center;">
                <h4 style="color:{t['primary']};">{icon('bi-award-fill')} Luar Biasa!</h4>
                <p style="color:{t['text']}">Tidak ada kata sulit yang terdeteksi hari ini. Semua bacaan lancar.</p>
            </div>
            """, unsafe_allow_html=True)

def render_ortu_monitoring():
    t = get_current_theme()
    st.markdown("<br>", unsafe_allow_html=True)
    c_btn, c_info = st.columns([1, 4])
    with c_btn:
        active = DataService.is_monitoring_active()
        if not active:
            if st.button("Mulai Sesi", type="primary", use_container_width=True):
                DataService.set_monitoring_active(True)
                st.rerun()
        else:
            if st.button("Stop Sesi", type="secondary", use_container_width=True):
                DataService.set_monitoring_active(False)
                st.rerun()
    
    with c_info:
        active = DataService.is_monitoring_active()
        if active:
            st.markdown(f"<div style='padding:8px; color:{t['primary']}; font-weight:600;'>{icon('bi-wifi', class_name='pulse-icon')} Device Connected (NARA-01)</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='padding:8px; color:{t['secondary']};'>{icon('bi-wifi-off')} Device Disconnected</div>", unsafe_allow_html=True)

    if DataService.is_monitoring_active():
        chart_place = st.empty()
        st.caption("Real-time Speech-to-Text Stream:")
        text_place = st.empty()
        
        sample_txt = "Budi sedang membaca buku di perpustakaan sekolah dengan tenang."
        words = sample_txt.split()
        current_words = []
        
        for i, w in enumerate(words):
            if not DataService.is_monitoring_active(): break
            chart_data = pd.DataFrame(np.random.uniform(0, 100, size=(1, 30))).T
            chart_place.bar_chart(chart_data, height=40, color=t['primary'])
            current_words.append(w)
            display_html = " ".join([f"<span class='highlight-active'>{word}</span>" if idx == i else word for idx, word in enumerate(current_words)])
            
            # Terminal always dark in original, but here we can make it dark or adapted. 
            # Original code: background-color: #1E293B (dark).
            # Let's keep a "terminal" look (Dark) or adapt to theme. Usually terminals are dark.
            # But "views/styles.py" .live-terminal defines it.
            # Let's trust .live-terminal CSS.
            
            text_place.markdown(f"""
            <div class="live-terminal">
                {icon('bi-mic-fill', color=t['accent'])} Listening...<br><br>
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
        DataService.set_monitoring_active(False)
        if st.button("Reset Monitor"): st.rerun()
    else:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding:60px; border: 2px dashed #CBD5E1; background-color:{t['background']};">
            {icon('bi-headset', size="3rem", color="#94A3B8")}
            <h5 style="color:{t['secondary']}; margin-top:15px; opacity: 0.8;">Monitoring Siap</h5>
            <p style="font-size:0.9rem; color:{t['secondary']}; opacity: 0.6;">Tekan tombol 'Mulai Sesi' untuk menghubungkan ke audio stream.</p>
        </div>
        """, unsafe_allow_html=True)

def view_ortu(student_name):
    t = get_current_theme()
    child_data = DataService.get_student_data(student_name)

    render_ortu_header(child_data)
    
    # Nav Style
    nav_bg = t['card_bg'] if st.session_state.get("theme_mode") == "light" else "transparent"
    nav_hover = "#F8FAFC" if st.session_state.get("theme_mode") == "light" else "#1E293B"

    selected_tab = option_menu(
        menu_title=None, 
        options=["Laporan Harian", "Live Monitoring"], 
        icons=["journal-text", "mic"], 
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": t['secondary'], "font-size": "14px"}, 
            "nav-link": {
                "font-size": "14px", 
                "text-align": "center", 
                "margin": "0px 10px 0px 0px", 
                "border-radius": "8px", 
                "background-color": nav_bg, 
                "border": f"1px solid {t['border']}", 
                "color": t['secondary'],
                "--hover-color": nav_hover
            },
            "nav-link-selected": {"background-color": t['primary'], "color": "white", "border": f"1px solid {t['primary']}"},
        }
    )

    if selected_tab == "Laporan Harian":
        render_ortu_report(child_data)
    elif selected_tab == "Live Monitoring":
        render_ortu_monitoring()
