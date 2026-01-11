import streamlit as st
from views.styles import COLOR_PRIMARY, COLOR_SEC, COLOR_ACCENT
from views.components import icon

# --- 1. CSS Wajib ---
def inject_custom_css():
    st.markdown(f"""
    <style>
    .soft-card {{
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #E0E0E0;
        margin-bottom: 20px;
        color: #333333;
    }}
    .soft-card h5 {{
        color: {COLOR_PRIMARY} !important;
        font-weight: 700;
        font-size: 1.1rem;
        margin-top: 15px;
        margin-bottom: 8px;
    }}
    .soft-card ul {{
        margin-left: 20px;
        margin-bottom: 15px;
    }}
    .soft-card li {{
        margin-bottom: 5px;
        line-height: 1.5;
    }}
    </style>
    """, unsafe_allow_html=True)

def render_section_header(title, icon_name):
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; margin-top: 30px;">
        <div style="background: {COLOR_PRIMARY}; padding: 10px; border-radius: 10px; color: white;">
            {icon(icon_name, size="1.5rem")}
        </div>
        <h3 style="margin: 0; color: {COLOR_PRIMARY};">{title}</h3>
    </div>
    """, unsafe_allow_html=True)

def section_guru():
    render_section_header("Panduan Guru", "bi-person-video3")
    
    # PERHATIKAN: HTML dirapatkan tanpa baris kosong di antaranya
    html_content = f"""
<div class="soft-card">
    <h5 style="margin-top:0;">1. Dashboard Kelas</h5>
    <p>Halaman utama guru menampilkan ringkasan performa siswa di kelas 1-A.</p>
    <ul>
        <li><b>Total Siswa</b>: Jumlah siswa aktif.</li>
        <li><b>Rata-rata Kelas</b>: Persentase kelancaran membaca rata-rata seluruh siswa.</li>
        <li><b>Perlu Bantuan</b>: Jumlah siswa dengan skor kelancaran di bawah 50%.</li>
        <li><b>Top XP</b>: Skor XP tertinggi yang dicapai siswa hari ini.</li>
    </ul>
    <h5>2. Daftar Siswa & Detail</h5>
    <p>Di bagian bawah, terdapat tabel daftar siswa.</p>
    <ul>
        <li>Klik salah satu baris siswa untuk melihat <b>Detail Siswa</b>.</li>
        <li>Detail mencakup: Grafik progress mingguan, Analisis AI, dan Kata Sulit yang perlu dilatih.</li>
    </ul>
</div>"""
    
    st.markdown(html_content, unsafe_allow_html=True)

def section_ortu():
    render_section_header("Panduan Orang Tua", "bi-house-heart")
    
    # PERHATIKAN: HTML dirapatkan tanpa baris kosong di antaranya
    html_content = f"""
<div class="soft-card">
    <h5 style="margin-top:0;">1. Memilih Siswa</h5>
    <p>Di sidebar (menu kiri), pilih nama anak Anda pada dropdown "Pilih Siswa".</p>
    <h5>2. Laporan Harian</h5>
    <p>Tab ini menampilkan hasil belajar anak hari ini:</p>
    <ul>
        <li><b>Skor Kelancaran</b>: Nilai bacaan anak dalam persen.</li>
        <li><b>Analisis NARA AI</b>: Feedback otomatis tentang kejelasan pengucapan.</li>
        <li><b>Kata Sulit</b>: Daftar kata yang terdeteksi salah ucap atau kurang jelas.</li>
    </ul>
    <h5>3. Live Monitoring</h5>
    <p>Gunakan fitur ini saat anak sedang belajar membaca:</p>
    <ul>
        <li>Tekan tombol <b>Mulai Sesi</b> untuk mengaktifkan monitoring.</li>
        <li>Sistem akan mendengarkan dan menampilkan teks secara real-time.</li>
        <li>Kata yang sedang dibaca akan di-highlight.</li>
        <li>Tekan <b>Stop Sesi</b> setelah selesai.</li>
    </ul>
</div>"""

    st.markdown(html_content, unsafe_allow_html=True)

def view_manual():
    # 1. Panggil CSS Injection
    inject_custom_css()
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: {COLOR_PRIMARY};">Buku Panduan Pengguna</h1>
        <p style="color: {COLOR_SEC};">NARA School Analytics System</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Guru", "Orang Tua"])
    
    with tab1:
        section_guru()
        
    with tab2:
        section_ortu()