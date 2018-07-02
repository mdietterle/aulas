#crime.py
import folium
import pandas as pd

coordenadas =(37.76, -122.45)
crimedata = pd.read_csv("C:\\Users\\Martim\\OneDrive\\Scripts Python\\aulas\\violencia\\dados.csv")
map = folium.Map(location=SF_COORDINATES, zoom_start=12)

casa = folium.simple_marker(
	location=[-26.4853, -49.067226],
	clustered_marker = True).add_to(brasil)
casa2 = folium.simple_marker(
	location=[-26.4853, -49.067226],
	clustered_marker = True).add_to(brasil)
casa3 = folium.simple_marker(
	location=[-26.4853, -49.067226],
	clustered_marker = True).add_to(brasil)
brasil.save(outfile="C:\\Users\\Martim\\OneDrive\\Scripts Python\\aulas\maps\\mapa2.html")
