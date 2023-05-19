## GeoJSON to JSONL Converter

This repository contains a Python script that converts GeoJSON files to JSONL (JSON Lines) format, with a specific focus on preserving the geometry data. JSONL format represents each JSON object as a separate line, which can be useful for streaming and processing large datasets.

### Usage

To use the converter script, follow these steps:

1. Install the required dependencies by running the following command:

   ```
   !pip install geopandas
   ```

2. Place your GeoJSON file in the same directory as the script.

3. Update the script with the filename of your GeoJSON file:

   ```python
   with open('input.geojson') as file:
       data = json.load(file)
   ```

   Replace `'input.geojson'` with the filename of your GeoJSON file.

4. Run the script.

   The script will read the GeoJSON file, convert each feature to JSONL format, and save the result in the `output.jsonl` file.

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
