import streamlit as st
st.set_page_config(
    page_title="ClimateCrop",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>

#MainMenu, header, footer {
    display: none !important;
}

html, body, .stApp, .stAppViewContainer, .main, .block-container {
    margin: 0 !important;
    padding: 0 !important;
    background: transparent !important;
    max-width: 100% !important;
}

/* Fix for background flickers */
body {
    background-color: #0a1e0f !important;
}


.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100vw;
    height: 100vh;
    background-image: 
        linear-gradient(
            rgba(10, 30, 15, 0.55),
            rgba(10, 30, 15, 0.70)
        ),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=2000&q=85");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    z-index: -1;
}


.landing {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    box-sizing: border-box;
    padding: 40px 25px 120px;
    background: transparent !important;
    position: relative;
    z-index: 1;
}

.logo {
    color: white !important;
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 25px;
    text-shadow: 0 3px 15px rgba(0,0,0,0.6);
}

.title {
    color: white !important;
    font-size: clamp(45px, 7vw, 72px);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 20px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.6);
}

.title span {
    color: #9be15d !important;
}

.subtitle {
    color: #eeeeee !important;
    font-size: clamp(16px, 2vw, 21px);
    max-width: 700px;
    line-height: 1.6;
    margin-bottom: 20px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.7);
}

.topic {
    color: #ffffff !important;
    font-size: clamp(14px, 1.5vw, 17px);
    font-weight: 500;
    letter-spacing: 1px;
    max-width: 700px;
    line-height: 1.5;
    margin-top: 5px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}

div[data-testid="stMarkdownContainer"] {
    background: transparent !important;
}



div[data-testid="stButton"] {
    position: fixed !important;
    right: 25px !important;
    bottom: 25px !important;
    width: auto !important;
    z-index: 9999 !important;
}

div[data-testid="stButton"] button {
    background: #8bc34a !important;
    color: white !important;
    border: none !important;
    border-radius: 30px !important;
    padding: 10px 22px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    width: auto !important;
    min-width: 0 !important;
    box-shadow: 0 5px 15px rgba(0,0,0,0.35) !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stButton"] button:hover {
    background: #6fa52f !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.45) !important;
}

/* Responsive Adjustments */
@media (max-width: 600px) {
    .landing {
        padding: 30px 20px 100px;
    }
    .logo {
        font-size: 18px;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }
    .title {
        font-size: 44px;
        margin-bottom: 15px;
    }
    .subtitle {
        font-size: 16px;
        max-width: 350px;
    }
    .topic {
        font-size: 13px;
        max-width: 330px;
    }
    div[data-testid="stButton"] {
        right: 15px !important;
        bottom: 15px !important;
    }
    div[data-testid="stButton"] button {
        padding: 8px 16px !important;
        font-size: 13px !important;
    }
}

</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """<div class="landing">
    <div class="logo">🌾 CLIMATECROP</div>
    <div class="title">Climate<span>Crop</span></div>
    <div class="subtitle">Predicting crop yield using climate and agricultural data with Machine Learning.</div>
    <div class="topic">Climate Change Impact on Crop Yield Prediction</div>
</div>""",
    unsafe_allow_html=True,
)

if st.button("🚀 Go to Website"):
    st.switch_page("pages/prediction.py")