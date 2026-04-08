# Read in a file from a URL and save a local CSV file with the first 10 rows
#

import time

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

def load_csv(filepath):
    print(f"loading data from {filepath}...")
    start_time = time.time()
    try:
        df = pd.read_csv(filepath, engine='pyarrow')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"number of rows: {len(df)}")
        print(f"number of columns: {len(df.columns)}")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

#Call load_csv to load 
filename = "sales_data_test.csv"
sales_data = load_csv(filename)

print(sales_data.head(10))