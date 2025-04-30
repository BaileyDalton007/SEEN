import pandas as pd
import numpy as np

"""
Load an IDEA dataset CSV file into a dataframe with some built in preprocessing.

Args:
    file_name: file name of the csv in the raw_data folder to import
    skip_rows: number of rows to skip at the top of the csv document
    null_vals: values to replace with null
    column_mappings: dictionary that maps column names defined in the csv to the desired column names
    drop_columns: list of column names to drop

Returns:
    A pandas dataframe with the loaded IDEA data
"""
def load_IDEA(file_name, skip_rows=0, null_vals=[-8, -9], column_mappings=None, drop_columns=None):
    file_path = 'raw_data/' + file_name

    # the IDEA data often has notes at the top of the CSV, drop them from the dataframe.
    df = pd.read_csv(file_path, skiprows=skip_rows)

    # replace certain values with NaNs, described in the data notes.
    df = df.replace(null_vals, np.nan)

    # drop any specified columns.
    if drop_columns:
        df = df.drop(drop_columns, axis=1)

    # if given a dictionary mapping orginal column names to new ones, rename them.
    if column_mappings:
        df = df.rename(columns=column_mappings)

    return df