import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------
#  PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Smart Indoor Air Quality Monitor",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏫 Smart Classroom Ventilation & Air Quality Dashboard")
st.markdown("### Prototype with User Inputs (No Sensors Yet)")
st.markdown("Enter simulated air quality readings below to check ventilation status.")

# -------------------------------
#  USER INPUT SECTION
# -------------------------------
col1, col2, col3, col4 = st.columns(4)
co2 = col1.number_input("CO₂ (ppm)", min_value=300, max_value=5000, value=800)
pm25 = col2.number_input("PM2.5 (µg/m³)", min_value=0, max_value=500, value=35)
temp = col3.number_input("Temperature (°C)", min_value=0, max_value=50, value=25)
hum = col4.number_input("Humidity (%)", min_value=0, max_value=100, value=50)

if st.button("Check Ventilation"):
    st.subheader("📊 Current Air Quality Status")

    # Display Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("CO₂ (ppm)", f"{co2}", "⚠️" if co2 > 1000 else "✅")
    m2.metric("PM2.5 (µg/m³)", f"{pm25}", "⚠️" if pm25 > 55 else "✅")
    m3.metric("Temperature (°C)", f"{temp}", "🌡️")
    m4.metric("Humidity (%)", f"{hum}", "💧")

    # -------------------------------
    #  VISUALIZATION
    # -------------------------------
    st.markdown("### 📈 Visual Overview")

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.bar(["CO₂", "PM2.5", "Temp", "Humidity"], [co2, pm25, temp, hum],
           color=["red" if co2 > 1000 else "green",
                  "red" if pm25 > 55 else "green",
                  "orange",
                  "blue"])
    ax.set_ylabel("Levels")
    ax.set_title("Indoor Air Quality Parameters")
    st.pyplot(fig)

    # -------------------------------
    #  ALERT CONDITIONS
    # -------------------------------
    alert_message = None
    if co2 > 1000 or pm25 > 55 or hum < 35 or hum > 65:
        alert_message = "🚨 Poor Ventilation Detected! Please open windows or turn on exhaust fans."
    else:
        alert_message = "✅ Ventilation is Good. Air quality within safe range."

    st.markdown(f"### 💡 Status: {alert_message}")

    # -------------------------------
    #  SOUND ALERT (Web-Compatible)
    # -------------------------------
    if "Poor" in alert_message:
        # Play alert sound using Streamlit's audio player
        try:
            st.audio("alert.mp3", format="audio/mp3")
        except:
            pass  # If audio file not found, continue without it
        
        st.error("⚠️ Alert! Ventilation is Poor.")
    else:
        st.success("✅ Everything looks fine.")

# -------------------------------
#  FOOTER
# -------------------------------
st.markdown("---")
st.markdown("👨‍🔬 *Developed as a Smart Ventilation Prototype – detects poor indoor air quality through user inputs.*")
