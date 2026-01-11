# Colors Updated
COLOR_PRIMARY = "#0F766E"    # Deep Emerald
COLOR_SEC = "#334155"        # Slate Dark
COLOR_BG = "#F1F5F9"         # Off-white / Blue Gray Tint
COLOR_ACCENT = "#F97316"     # Coral Orange

# PERUBAHAN DI SINI:
# Mengganti Pure White (#FFFFFF) menjadi Slate-50 (#F8FAFC)
# Ini mengurangi "glare" tapi tetap terlihat sebagai kartu yang terang.
COLOR_WHITE = "#F8FAFC"      

def get_custom_css():
    return f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Poppins:wght@500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: {COLOR_SEC};
        background-color: {COLOR_BG};
    }}
    
    h1, h2, h3, h4 {{
        font-family: 'Poppins', sans-serif;
        color: {COLOR_PRIMARY};
        font-weight: 600;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    .soft-card {{
        background-color: {COLOR_WHITE};
        border-radius: 16px;
        padding: 24px;
        /* Mengurangi opacity shadow sedikit agar depth-nya tidak terlalu keras */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        /* Border dibuat lebih transparan agar menyatu */
        border: 1px solid rgba(255,255,255,0.6);
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }}
    .soft-card:hover {{
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }}

    .metric-label {{
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #64748B;
        margin-bottom: 5px;
    }}
    .metric-value {{
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: {COLOR_PRIMARY};
    }}
    .metric-delta {{
        font-size: 0.8rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 4px;
    }}
    
    .alert-box {{
        background-color: #FFF7ED; 
        border-left: 4px solid {COLOR_ACCENT};
        padding: 16px;
        border-radius: 8px;
        color: #9A3412;
    }}
    
    .suggestion-box {{
        background-color: #F0FDFA; 
        border: 1px dashed {COLOR_PRIMARY};
        border-radius: 12px;
        padding: 16px;
    }}

    .word-tag {{
        display: inline-flex;
        align-items: center;
        background-color: #FFEDD5; 
        color: #C2410C; 
        padding: 4px 12px;
        border-radius: 99px;
        margin: 4px 4px 4px 0;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #FED7AA;
    }}

    .live-terminal {{
        background-color: #1E293B; 
        color: #E2E8F0;
        font-family: 'Courier New', Courier, monospace;
        padding: 25px;
        border-radius: 12px;
        min-height: 120px;
        border-left: 6px solid {COLOR_PRIMARY};
    }}
    .highlight-active {{
        background-color: {COLOR_ACCENT};
        color: white;
        padding: 2px 6px;
        border-radius: 4px;
    }}
    .pulse-icon {{
        animation: pulse-animation 2s infinite;
        color: {COLOR_ACCENT};
    }}
    @keyframes pulse-animation {{
        0% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}
</style>
"""