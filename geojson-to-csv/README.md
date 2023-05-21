# GeoJSON to CSV Converter

This repository contains a Python script that converts GeoJSON files to CSV format, preserving the geometry information in Well-Known Text (WKT) representation. The script utilizes the `geopandas` library to handle the GeoJSON data and perform the conversion.

## Usage

To use the converter script, follow these steps:

1. Install the required dependencies by running the following command:

   ```
   pip install geopandas pandas
   ```

2. Place your GeoJSON file in the same directory as the script.

3. Update the script with the filename of your GeoJSON file and the desired output CSV filename:

   ```python
   # Define file paths
   input_file = 'input.geojson'
   output_file = 'output.csv'
   ```

   Replace `'input.geojson'` with the filename of your GeoJSON file, and `'output.csv'` with the desired filename for the output CSV file.

4. If your GeoJSON file has a different geometry field name (e.g., `'geom'`, `'shape'`), you can specify it by updating the `geometry_field` variable in the script:

   ```python
   # User-defined geometry field name
   geometry_field = 'geometry'
   ```

   Replace `'geometry'` with the appropriate geometry field name.

5. Run the script.

   The script will read the GeoJSON file, convert it to CSV format with the specified geometry field, and save the result in the output CSV file.

## Dependencies

The script has the following dependencies:

- Python 3.9.6
- `geopandas` library
- `pandas` library

Make sure you have the required dependencies installed before running the script. You can install them using `pip install geopandas pandas`.

## Open-Source

This project is open-source, meaning you are free to use, modify, and distribute the code.

## Acknowledgments

The script utilizes the `geopandas` and `pandas` libraries for reading, processing, and converting GeoJSON data. Special thanks to the `geopandas` and `pandas` communities for their contributions.

For more information on `geopandas`, refer to the [official documentation](https://geopandas.org/).
