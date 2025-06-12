import streamlit as st
import math

# Title of the app
st.title("Wet Bulb Temperature Calculator")
st.markdown("Calculate the wet bulb temperature (WBT) based on air temperature and relative humidity.")

# Input fields
temp_celsius = st.number_input("Air Temperature (°C)", min_value=-50.0, max_value=60.0, value=30.0, step=0.1, format="%.1f")
rel_humidity = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1, format="%.1f")

# Calculation function
def calculate_wbt(T, RH):
    return (
        T * math.atan(0.151977 * (RH + 8.313659) ** 0.5)
        + math.atan(T + RH)
        - math.atan(RH - 1.676331)
        + 0.00391838 * RH ** 1.5 * math.atan(0.023101 * RH)
        - 4.686035
    )

# Calculation and output
if st.button("Calculate"):
    wbt = calculate_wbt(temp_celsius, rel_humidity)
    st.success(f"The wet bulb temperature is approximately {wbt:.1f} °C")
