import pandas
import folium

data = pandas.read_json('coordinates.json')

lat = data['DD']['lat']
log = data['DD']['lng']
dataCollections = data["DD"]['popup']

testmap = folium.Map(location=[3.1465, 101.6923], zoom_start=10, title='Stamen Terrain')

record = folium.FeatureGroup(name='COVID')

# looping through every cordinate and popup message in the JSON file
for lt, lg, dc in zip(lat, log, dataCollections):
    record.add_child(folium.Marker(location=[lt, lg], popup=dc))

Border = folium.FeatureGroup(name="Populations")
# GeoJson for border of the malaysia
data = open('package.json', 'r', encoding='utf-8-sig').read()
Border.add_child(folium.GeoJson(data, style_function=lambda x: {
    'fillColor': '#00ff00' if x['properties']['ISO3'] == 'MYS' else '#000000'}))

testmap.add_child(record)
testmap.add_child(Border)
testmap.add_child(folium.LayerControl())

testmap.save('map2.html')
