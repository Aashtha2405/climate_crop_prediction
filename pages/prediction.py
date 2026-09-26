import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
st.set_page_config(
    page_title="ClimateCrop",
    page_icon="🌾",
    layout="wide"
)
df = pd.read_csv("dataset.csv")
model = joblib.load("crop_yield_model.pkl")
feature_columns = joblib.load("model_features.pkl")
st.markdown("""
<style>
.main {
    background-color: #f5f8f2;
}
.title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}
.result {
    padding: 30px;
    border-radius: 20px;
    background-color: green;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="title">🌾 ClimateCrop</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">'
    'Climate Change Impact on Crop Yield Prediction'
    '</div>',
    unsafe_allow_html=True
)
st.write("")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        "📊 Dataset Records",
        len(df)
    )
with col2:
    st.metric(
        "🌡️ Climate Features",
        "4"
    )
with col3:
    st.metric(
        "🌾 Crops",
        df["Crop"].nunique()
    )
with col4:
    st.metric(
        "📍 States",
        df["State"].nunique()
    )
st.header("🌱 Crop Yield Prediction")
col1, col2 = st.columns(2)
with col1:
    year = st.number_input(
        "📅 Year",
        min_value=2000,
        max_value=2100,
        value=2026
    )
    state = st.selectbox(
        "📍 State",
        sorted(df["State"].unique())
    )
    crop = st.selectbox(
        "🌾 Crop",
        sorted(df["Crop"].unique())
    )
    temperature = st.number_input(
        "🌡️ Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=30.0
    )
with col2:

    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
        max_value=5000.0,
        value=900.0
    )

    humidity = st.number_input(
        "💧 Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

    co2 = st.number_input(
        "🌍 CO₂ (ppm)",
        min_value=200.0,
        max_value=1000.0,
        value=420.0
    )

    area = st.number_input(
        "🌱 Area (hectares)",
        min_value=1.0,
        max_value=100000.0,
        value=1000.0
    )

input_data = pd.DataFrame({
    "Year": [year],
    "Temperature_C": [temperature],
    "Rainfall_mm": [rainfall],
    "Humidity_pct": [humidity],
    "CO2_ppm": [co2],
    "Area_hectares": [area]
})
for col in feature_columns:
    if col.startswith("State_"):
        state_name = col.replace("State_", "")
        input_data[col] = int(state == state_name)
    elif col.startswith("Crop_"):
        crop_name = col.replace("Crop_", "")
        input_data[col] = int(crop == crop_name)
input_data = input_data.reindex(
    columns=feature_columns,
    fill_value=0
)
st.write("")
predict_button = st.button(
    "🔮 Predict Crop Yield",
    use_container_width=True
)
if predict_button:
    prediction = model.predict(input_data)[0]
    st.markdown(
        f"""
        <div class="result">
        <h2>🌾 Predicted Crop Yield</h2>
        <h1>{prediction:,.2f} kg/hectare</h1>
        <p>
        Location: {state} |
        Crop: {crop}
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
st.header("🌍 Climate & Crop Yield Analysis")
fig = px.scatter(
    df,
    x="Temperature_C",
    y="Yield_kg_per_hectare",
    color="Crop",
    hover_data=["State", "Year"],
    title="Temperature vs Crop Yield"
)
st.plotly_chart(
    fig,
    use_container_width=True
)
fig = px.scatter(
    df,
    x="Rainfall_mm",
    y="Yield_kg_per_hectare",
    color="Crop",
    hover_data=["State"],
    title="Rainfall vs Crop Yield"
)
st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()
st.header("🌍 Climate Change Scenario")
st.write(
    "Compare crop yield under normal and changed climate conditions."
)
scenario_col1, scenario_col2 = st.columns(2)
with scenario_col1:
    scenario_temp = st.number_input(
        "Changed Temperature (°C)",
        value=temperature + 3
    )
    scenario_rainfall = st.number_input(
        "Changed Rainfall (mm)",
        value=rainfall * 0.9
    )
with scenario_col2:
    scenario_humidity = st.number_input(
        "Changed Humidity (%)",
        value=max(0.0, humidity - 5)
    )

    scenario_co2 = st.number_input(
        "Changed CO₂ (ppm)",
        value=co2 + 30
    )
scenario_data = pd.DataFrame({
    "Year": [year],
    "Temperature_C": [scenario_temp],
    "Rainfall_mm": [scenario_rainfall],
    "Humidity_pct": [scenario_humidity],
    "CO2_ppm": [scenario_co2],
    "Area_hectares": [area]
})
for col in feature_columns:

    if col.startswith("State_"):

        state_name = col.replace("State_", "")
        scenario_data[col] = int(state == state_name)

    elif col.startswith("Crop_"):

        crop_name = col.replace("Crop_", "")
        scenario_data[col] = int(crop == crop_name)
scenario_data = scenario_data.reindex(
    columns=feature_columns,
    fill_value=0
)
if st.button(
    "🌍 Analyze Climate Impact",
    use_container_width=True
):
    normal_prediction = model.predict(input_data)[0]
    changed_prediction = model.predict(scenario_data)[0]
    percentage_change = (
        (changed_prediction - normal_prediction)
        / normal_prediction
    ) * 100
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Normal Yield",
            f"{normal_prediction:,.2f} kg/ha"
        )
    with col2:
        st.metric(
            "Changed Climate Yield",
            f"{changed_prediction:,.2f} kg/ha"
        )
    with col3:
        st.metric(
            "Yield Change",
            f"{percentage_change:.2f}%"
        )
st.divider()
st.markdown(
    """
    <center>
    🌾 <b>ClimateCrop</b><br>
    ML Project Based Crop Yield Prediction<br>
    <small>Climate Change Impact on Agriculture</small>
    </center>
    """,
    unsafe_allow_html=True
)