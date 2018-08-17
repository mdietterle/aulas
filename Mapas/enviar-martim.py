import pandas as pd
import folium
import requests
import json
from folium.plugins import MarkerCluster


mapa = folium.Map(
    location=[-16.1237611, -59.9219642],
    zoom_start=4)

marcador = MarkerCluster().add_to(mapa)

csv = pd.read_csv('importar1.csv', encoding = 'latin-1', delimiter= ';')
cepsjgs = pd.read_csv('cepsjaragua2.csv', encoding= 'latin-1', delimiter=";")

crimes = csv[csv['CIDADE'] != '']
ceps = cepsjgs[cepsjgs['CEP'] != '']

for _, csv in crimes.iterrows():

    url = 'https://nominatim.openstreetmap.org/search.php?q=' + csv['CIDADE'] + '&polygon_geojson=1&limit=1&format=json'
    r = requests.get(url)
    res = r.json()

    for dados in res:
        lat = float(dados['lat'])
        lon = float(dados['lon'])
        coords = dados['geojson']
        posicao = dados['boundingbox']

        #marcando pontos
        print(csv['CIDADE'])
        for hd in range(csv["MV HOMICIDIO DOLOSO"]):
            for _, cep in ceps.iterrows():
                url2 = 'https://nominatim.openstreetmap.org/search.php?q=' + ceps['CEP']
                c = requests.get(url2)
                res2 = c.json()
                for ponto in res2:
                    lat2=float(ponto['lat'])
                    lon2 = float(ponto['lon'])
                    folium.Marker([lat2,lon2]).add_to(marcador)
    mapa.choropleth(geo_data=coords, fill_color='YlOrRd', fill_opacity=0.2, line_opacity=0.8)



mapa.save('map.html')
