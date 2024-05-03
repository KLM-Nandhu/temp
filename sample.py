import streamlit as st
import requests

def fetch_real_time_weather(location):
    api_key = '053e023d688ca4c6e94377b9e87340fffc51f99d5ef47e84620e8ab0ebd2e629'
    query = f"weather {location}"
    url = f"https://serpapi.com/search.json?q={query}&hl=en&gl=in&api_key={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_results = data.get('answer_box', {})
            if weather_results:
                weather = weather_results.get('weather', 'Not available')
                temperature = weather_results.get('temperature', 'Not available')
                humidity = weather_results.get('humidity', 'Not available')
                wind = weather_results.get('wind', 'Not available')
                date_time = weather_results.get('date', 'Date and time not specified')
                return {
                    "Weather": weather,
                    "Temperature": f"{temperature}°C",
                    "Humidity": f"{humidity}%",
                    "Wind": wind,
                    "Date and Time": date_time
                }
            else:
                return "Weather data not found in the API response."
        else:
            return f"Failed to fetch weather data. Status Code: {response.status_code}"
    except Exception as e:
        return f"An error occurred while fetching the weather data: {str(e)}"

# Streamlit UI components
st.title('KLM WEATHER APP')
location = st.text_input('Enter the location', '')

if st.button('Fetch Weather'):
    if location:
        result = fetch_real_time_weather(location)
        if isinstance(result, dict):
            st.subheader("This Is Your Weather")
            for key, value in result.items():
                st.text(f"{key}: {value}")
        else:
            st.error(result)
    else:
        st.error("Please enter a location.")