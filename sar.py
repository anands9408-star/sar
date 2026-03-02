import streamlit as st
import folium
from streamlit_folium import st_folium
import numpy as np

# Set up the dashboard title
st.set_page_config(page_title="SAR Prediction Platform", layout="wide")
st.title("🛩️ Aircraft SAR Prediction Platform (S31)")

# Sidebar for user inputs (Last Known Coordinates)
st.sidebar.header("Input Mission Data")
target_lat = st.sidebar.number_input("Last Known Latitude", value=12.9716)
target_lon = st.sidebar.number_input("Last Known Longitude", value=77.5946)
altitude = st.sidebar.slider("Current Altitude (ft)", 5000, 40000, 30000)

# Create the map
st.subheader("Probabilistic Search Zones & Resource Allocation")
m = folium.Map(location=[target_lat, target_lon], zoom_start=12)

# Simulate Probability Zones (Alpha, Beta, Gamma)
folium.Circle([target_lat, target_lon], radius=2000, color='red', fill=True, popup='Alpha Zone (High Prob)').add_to(m)
folium.Circle([target_lat, target_lon], radius=5000, color='orange', fill=False, popup='Beta Zone').add_to(m)
folium.Circle([target_lat, target_lon], radius=8000, color='yellow', fill=False, popup='Gamma Zone').add_to(m)

# Add Marker for Last Known Position
folium.Marker([target_lat, target_lon], icon=folium.Icon(color='red', icon='plane')).add_to(m)

# Display the map in Streamlit
st_folium(m, width=900, height=500)

# Resource Allocation Table
st.table({
    "Search Sector": ["Alpha", "Beta", "Gamma"],
    "Probability (%)": [70, 20, 10],
    "Assigned Resource": ["Drone Squad A", "Helicopter 01", "Ground Team"]
})

# Simple Glide Physics for S31
glide_ratio = 15  # Standard for many aircraft
search_radius = (altitude / 3280.84) * glide_ratio  # Converts feet to km

st.write(f"### Predicted Search Radius: {search_radius:.2f} km")

