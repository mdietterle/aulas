import folium
import pandas as pd

brasil = folium.Map(
	location=[-26.4853, -49.067226],
	zoom_start=12
	)
casa = folium.Marker(
	location=[-26.4853, -49.067226],
	).add_to(brasil)
brasil.save(outfile="mapa.html")