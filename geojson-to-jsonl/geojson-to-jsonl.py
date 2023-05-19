import json
import geopandas as gpd

# Read in geojson file
with open('Local_Authority_Districts_(May_2023)_UK_BFE.geojson') as file:
    data = json.load(file)

# Create empty list to store features
output = []
for feature in data['features']:
    # Include the "geometry" field in each feature
    feature['geometry'] = feature.get('geometry', {})
    output.append(json.dumps(feature))

# Write to file
with open('output.jsonl', 'w') as file:
    file.write('\n'.join(output))
