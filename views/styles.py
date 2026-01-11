import streamlit as st

# Theme Configurations
THEMES = {
    "light": {
        "primary": "#0F766E",      # Deep Emerald
        "secondary": "#334155",    # Slate Dark
        "background": "#F1F5F9",   # Off-white / Blue Gray Tint
        "card_bg": "#FFFFFF",      # Pure White for crisp cards
        "text": "#334155",         # Dark Slate
        "accent": "#F97316",       # Coral Orange
        "border": "rgba(0,0,0,0.05)",
        "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)"
    },
    "dark": {
        "primary": "#14B8A6",      # Lighter Emerald for Dark Mode
        "secondary": "#E2E8F0",    # Light Slate
        "background": "#0F172A",   # Slate 900
        "card_bg": "#1E293B",      # Slate 800
        "text": "#F1F5F9",         # Light text
        "accent": "#FB923C",       # Lighter Orange
        "border": "rgba(255,255,255,0.1)",
        "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.3)"
    }
}

# Backwards Compatibility (Default to Light)
COLOR_PRIMARY = THEMES["light"]["primary"]
COLOR_SEC = THEMES["light"]["secondary"]
COLOR_BG = THEMES["light"]["background"]
COLOR_ACCENT = THEMES["light"]["accent"]
COLOR_WHITE = THEMES["light"]["card_bg"]

def get_current_theme():
    # Helper to get the current theme dict based on session state
    mode = st.session_state.get("theme_mode", "light")
    return THEMES[mode]

# Default to light for initial load or static references if needed
CURRENT_THEME = THEMES["light"]

def get_custom_css(theme_mode="light"):
    t = THEMES[theme_mode]
    
    return f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700;800&display=swap');

    :root {{
        --primary: {t['primary']};
        --secondary: {t['secondary']};
        --bg: {t['background']};
        --card-bg: {t['card_bg']};
        --text: {t['text']};
        --accent: {t['accent']};
    }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: {t['text']};
        background-color: {t['background']};
    }}
    
    /* Global Headings */
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Poppins', sans-serif;
        color: {t['text']}; /* Use text color by default, specific headers can be primary */
    }}
    
    /* Streamlit Overrides */
    .stApp {{
        background-color: {t['background']};
    }}
    
    /* Hide Default Elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display:none;}}
    
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    /* --- CARDS --- */
    .soft-card {{
        background-color: {t['card_bg']};
        border-radius: 16px;
        padding: 24px;
        box-shadow: {t['shadow']};
        border: 1px solid {t['border']};
        margin-bottom: 1rem;
        transition: all 0.2s ease;
    }}
    .soft-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }}

    /* --- METRICS --- */
    .metric-label {{
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: {t['secondary']};
        opacity: 0.8;
        margin-bottom: 5px;
    }}
    .metric-value {{
        font-family: 'Poppins', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: {t['text']}; /* Stronger contrast */
    }}
    .metric-delta {{
        font-size: 0.8rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 4px;
    }}
    
    /* --- ALERTS & TAGS --- */
    .alert-box {{
        background-color: {t['card_bg']}; 
        border-left: 4px solid {t['accent']};
        padding: 16px;
        border-radius: 8px;
        color: {t['text']};
        border: 1px solid {t['border']};
    }}
    
    .suggestion-box {{
        background-color: {t['background']};
        border: 1px dashed {t['primary']};
        border-radius: 12px;
        padding: 16px;
    }}

    .word-tag {{
        display: inline-flex;
        align-items: center;
        background-color: {t['background']}; 
        color: {t['accent']}; 
        padding: 6px 14px;
        border-radius: 99px;
        margin: 4px 4px 4px 0;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid {t['accent']}33; /* 20% opacity */
    }}

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {{
        background-color: {t['card_bg']};
        border-right: 1px solid {t['border']};
    }}
    
    /* --- TABLE --- */
    [data-testid="stDataFrame"] {{
        border: 1px solid {t['border']};
        border-radius: 8px;
        overflow: hidden;
    }}

    /* --- ANIMATIONS --- */
    .pulse-icon {{
        animation: pulse-animation 2s infinite;
        color: {t['accent']};
    }}
    @keyframes pulse-animation {{
        0% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}
</style>
"""
