import pandas
import folium

data = pandas.read_json('coordinates(1).json')

lt = data['DD']['lat']
lg = data['DD']['lng']

testmap = folium.Map(location=[3.1465, 101.6923],zoom_start=10, title='Stamen Terrain')

record = folium.FeatureGroup(name='COVID')

record.add_child(folium.Marker(location=[lt,lg],popup="there is corona here"))

testmap.add_child(record)

testmap.save('map2.html')