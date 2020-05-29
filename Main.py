import folium
import pandas

data = pandas.read_csv('original.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['ELEV'])


def color_manageing(evl):
    if evl < 1000:
        return "green"
    elif 1000 <= evl <= 3000:
        return "orange"
    else:
        return 'red'


map = folium.Map(location=[46.885, -121.633], zoom_start=5, title='Stamen Terrain')

Vrecord = folium.FeatureGroup(name='my Map')

for lt, ln, nm in zip(lat, lon, name):
    Vrecord.add_child(folium.CircleMarker(radius=40, location=[lt, ln], popup=nm, fill=True, fill_color=color_manageing(nm),
                                   color=color_manageing(nm)))

Border = folium.FeatureGroup(name="Populations")

data=open('package.json', 'r', encoding='utf-8-sig').read()
Border.add_child(folium.GeoJson(data, style_function=lambda x:{'fillColor':'#00ff00' if x['properties']['ISO3'] == 'MYS' else '#000000' }))



map.add_child(Vrecord)
map.add_child(Border)
map.add_child(folium.LayerControl())

map.save('map.html')
