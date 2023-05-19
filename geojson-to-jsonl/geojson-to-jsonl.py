# Define file paths
input_file = 'Local_Authority_Districts_(May_2023)_UK_BFE.geojson'
output_file = 'output-2.jsonl'

# Import libraries
import json
import geopandas as gpd
import time

# Decorator function to measure execution time
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print("--- Time taken by {}: {} seconds ---".format(func.__name__, round(execution_time, 2)))
        return result
    return wrapper

@measure_execution_time
def read_geojson_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

@measure_execution_time
def process_features(data):
    # Add a new property to each feature
    output = [json.dumps(feature) for feature in data['features']]
    return output

@measure_execution_time
def write_to_file(output, file_path):
    with open(file_path, 'w') as file:
        file.write('\n'.join(output))

# Measure the time for each step
data = read_geojson_file(input_file)
output = process_features(data)
write_to_file(output, output_file)
