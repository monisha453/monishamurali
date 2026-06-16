import streamlit as st
import requests

st.title("🌤️ Weather App")

# Input box for city name
city = st.text_input("Enter city name")

# Your OpenWeatherMap API key (replace with your real API key)
API_KEY = "bd6d969423da4b63336f7c8c1c069648"  # <-- Replace with your actual API key

if st.button("Get Weather"):
    if city:
        # Build the API request URL
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        # Send request to the weather API
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extract data from the API response
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            
            # Display results
            st.write(f"🌡️ Temperature: {temp}°C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"☁️ Condition: {condition}")
        else:
            st.error("City not found or API key issue. Please try again.")
    else:
        st.warning("Please enter a city name.")