# Read in a file from a URL and save a local CSV file with the first 10 rows
#

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

df = pd.read_csv(filename, engine='pyarrow')

out_file = "sales_data.csv"
df.head(10).to_csv('first_10_rows.csv', index=False)