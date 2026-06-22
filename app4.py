import streamlit as st
import pandas as pd
import pickle
import base64

st.set_page_config(page_title="NeuroGuard AI", layout="wide")


def add_bg(image_file, dark1=0.45, dark2=0.70):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(3,7,18,{dark1}), rgba(3,7,18,{dark2})),
    url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

#MainMenu, footer, header {{
    visibility: hidden;
}}

.block-container {{
    padding-top: 1.5rem;
    max-width: 1300px;
}}

.landing {{
    min-height: 78vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}}

.landing h1 {{
    color: white;
    font-size: 76px;
    font-weight: 1000;
    letter-spacing: 6px;
    text-transform: uppercase;
    text-shadow: 0 0 35px rgba(37,99,235,0.9);
}}

.landing p {{
    color: #e0f2fe;
    font-size: 25px;
    font-weight: 600;
    line-height: 1.8;
    text-shadow: 0 0 18px black;
}}

.hero {{
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 35px;
    text-align: center;
    margin-bottom: 28px;
    box-shadow: 0 25px 70px rgba(0,0,0,0.45);
}}

.hero h1 {{
    color: white;
    font-size: 48px;
    font-weight: 900;
}}

.hero p {{
    color: #bfdbfe;
    font-size: 18px;
}}

.card {{
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 30px;
    box-shadow: 0 25px 60px rgba(0,0,0,0.40);
    margin-bottom: 24px;
}}

.title {{
    color: white;
    font-size: 28px;
    font-weight: 900;
    border-bottom: 2px solid #38bdf8;
    padding-bottom: 12px;
    margin-bottom: 25px;
}}

.info-box {{
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    margin-bottom: 18px;
}}

.info-box h3 {{
    color: #93c5fd;
    font-size: 15px;
}}

.info-box p {{
    color: white;
    font-size: 22px;
    font-weight: 900;
}}

.note {{
    color: #cbd5e1;
    background: rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    line-height: 1.7;
}}

label {{
    color: white !important;
    font-weight: 700 !important;
}}

.stNumberInput input {{
    background: white;
    color: #020617;
    border-radius: 14px;
    height: 45px;
    font-weight: 700;
}}

div[data-baseweb="select"] > div {{
    background: white;
    border-radius: 14px;
    min-height: 45px;
    font-weight: 700;
}}

div.stButton > button {{
    width: 100%;
    height: 60px;
    border-radius: 40px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white;
    font-size: 20px;
    font-weight: 900;
}}

.login-btn button {{
    width: 190px !important;
    height: 68px !important;
}}

.result-high {{
    background: rgba(220,38,38,0.45);
    color: #fecaca;
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
}}

.result-low {{
    background: rgba(22,163,74,0.45);
    color: #bbf7d0;
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
}}
</style>
""", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "home":
    add_bg("bg3.png", 0.25, 0.55)

    st.markdown("""
<div class="landing">
    <div>
        <h1>NEUROGUARD AI</h1>
        <p>Intelligent Drug Addiction Risk Prediction<br>Powered by Advanced Machine Learning Analytics</p>
    </div>
</div>
""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        st.markdown('<div class="login-btn">', unsafe_allow_html=True)
        if st.button("LOGIN"):
            st.session_state.page = "prediction"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


else:
    add_bg("bg2.png", 0.52, 0.75)

    model = pickle.load(open("best_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    feature_columns = pickle.load(open("feature_columns.pkl", "rb"))
    best_model_name = pickle.load(open("best_model_name.pkl", "rb"))

    st.markdown("""
<div class="hero">
    <h1>Drug Addiction Prediction System</h1>
    <p>Advanced Machine Learning Based Behavioral Risk Analysis</p>
</div>
""", unsafe_allow_html=True)

    left, right = st.columns([2.5, 1])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="title">Student Input Details</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)

        with c1:
            attendance = st.number_input("Attendance Percentage", 0, 100, 75)
            sleep = st.number_input("Sleep Hours", 0, 24, 6)
            stress = st.number_input("Stress Level", 1, 10, 5)

        with c2:
            academic = st.number_input("Academic Score", 0, 100, 70)
            family = st.number_input("Family Support Score", 1, 10, 5)
            screen = st.number_input("Screen Time Hours", 0, 24, 6)

        with c3:
            experiment = st.selectbox("Experimentation", ["No", "Yes"])
            decline = st.selectbox("Academic Performance Decline", ["No", "Yes"])
            social = st.selectbox("Social Isolation", ["No", "Yes"])

        c4, c5, c6 = st.columns(3)

        with c4:
            health = st.selectbox("Physical / Mental Health Problems", ["No", "Yes"])

        with c5:
            risk = st.selectbox("Risk Taking Behavior", ["No", "Yes"])

        with c6:
            withdrawal = st.selectbox("Withdrawal Symptoms", ["No", "Yes"])

        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="title">AI System Summary</div>', unsafe_allow_html=True)

        st.markdown(f"""
<div class="info-box">
    <h3>Machine Learning Model</h3>
    <p>{best_model_name}</p>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="info-box">
    <h3>Prediction Mode</h3>
    <p>Binary Classification</p>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="info-box">
    <h3>Output Result</h3>
    <p>Addiction Risk Level</p>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="note">
This intelligent prediction system analyzes student behavior, academic performance,
lifestyle habits, and risk indicators to estimate possible addiction risk.
</div>
""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    input_data = pd.DataFrame([{
        "Attendance_Percentage": attendance,
        "Sleep_Hours": sleep,
        "Stress_Level": stress,
        "Academic_Score": academic,
        "Family_Support_Score": family,
        "Screen_Time_Hours": screen,
        "Experimentation": experiment,
        "Academic_Performance_Decline": decline,
        "Social_Isolation": social,
        "Physical_Mental_Health_Problems": health,
        "Risk_Taking_Behavior": risk,
        "Withdrawal_Symptoms": withdrawal
    }])

    for col in [
        "Experimentation",
        "Academic_Performance_Decline",
        "Social_Isolation",
        "Physical_Mental_Health_Problems",
        "Risk_Taking_Behavior",
        "Withdrawal_Symptoms"
    ]:
        input_data[col] = input_data[col].map({"No": 0, "Yes": 1})

    input_data = input_data[feature_columns]
    input_data = scaler.transform(input_data)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.button("Predict Addiction Risk"):
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.markdown('<div class="result-high">High Addiction Risk Detected</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-low">Low Addiction Risk Detected</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)