# GeoJSON to JSONL Converter

This repository contains a Python script that converts GeoJSON files to JSONL (JSON Lines) format, while also measuring the execution time of each step. JSONL format represents each JSON object as a separate line, which can be useful for streaming and processing large datasets.

## Usage

To use the converter script, follow these steps:

1. Clone or download the repository to your local machine.

2. Ensure that you have the necessary dependencies installed. You can install the required dependencies by running the following command:

   ```
   pip install geopandas
   ```

3. Open the Python script named `geojson_to_jsonl.py` in your preferred editor.

4. Define the file paths for the input GeoJSON file and the desired output JSONL file:

   ```python
   # Define file paths
   input_file = 'input.geojson'
   output_file = 'output.jsonl'
   ```

   Replace `'input.geojson'` with the actual file path of your input GeoJSON file, and `'output.jsonl'` with the desired output file path.

5. Run the script.

   The script will read the GeoJSON file, process the features by adding a new property to each feature, measure the execution time of each step, and save the converted JSONL data to the output file. The execution time for each step will be printed in the console.

### Dependencies

The script has the following dependencies:

- Python 3.9.6
- `geopandas` library

Make sure you have the required dependencies installed before running the script.

### Open-Source

This project is open-source, which means you are free to use, modify, and distribute the code.

### Acknowledgments

The script utilizes the `geopandas` library for reading and processing GeoJSON data. Special thanks to the `geopandas` community for their contributions.

For more information on `geopandas`, refer to the [official documentation](https://geopandas.org/).
