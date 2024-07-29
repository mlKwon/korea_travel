
import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Load the provided CSV file with latitude and longitude
file_path = 'korean_travel_240720.csv'
travel_data = pd.read_csv(file_path, encoding='cp949')

# set the page title
st.set_page_config(page_title="Koreanesch Reeskaart fir Backes & Lippert Famill", layout="wide")

st.title("🗺️Korea reesen Kaart fir Lëtzebuerger🧳")
st.info("🖱️Dir kënnt detailléiert Informatioun iwwerpréiwen andeems Dir op d'Reesdestinatioun hovert oder klickt.")

# Initialize map
m = folium.Map(location=[36.5, 127.5], zoom_start=7)
# m = folium.Map(location=[36.5, 127.5], zoom_start=7, tiles='CartoDB positron')

# Add marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers to the map
for idx, row in travel_data.iterrows():
    location = f"{row['Location']}, {row['Contents']}"
    popup_text = f"""
    <div style='width: 300px;'>
    <b>{row['Location']}</b><br>
    English: {row['Contents']}<br>
    Korean: {row['Contents (Korean)']}<br>
    <a href="{row['URL']}" target="_blank">More info</a>
    """
    folium.Marker(
        location=[row['lat'], row['long']],
        popup=popup_text,
        tooltip=row['Location']
    ).add_to(marker_cluster)

# Display the map
folium_static(m)

