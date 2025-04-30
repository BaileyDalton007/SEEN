import pandas as pd
import numpy as np

OHIO_STATE_CODE = 390

"""
Load an (Ohio) District Profile Report dataset excel file into a dataframe with some built in preprocessing.
Args:
    file_name: file name of the csv in the raw_data folder to import
    column_mappings: dictionary that maps column names defined in the csv to the desired column names
    drop_columns: list of column names to drop
    keep_columns: list of column names to keep


Returns:
    A pandas dataframe with the loaded DPR data
"""
def load_DPR(file_name, column_mappings=None, drop_columns=None, keep_columns=None):
    file_path = 'raw_data/' + file_name

    df = pd.read_excel(file_path, sheet_name='District Data')

    # Converts the school district "IRN" to a LEAID that we use to join data.
    df['LEAID'] = (str(OHIO_STATE_CODE) + df['IRN'].astype('string').str[:4]).astype('int')

    # if keep columns is defined, keep just those columns.
    # otherwise, if drop columns is defined, drop those columns
    if keep_columns:
        df = df[keep_columns]
    elif drop_columns:
        df = df.drop(drop_columns, axis=1)

    # if given a dictionary mapping orginal column names to new ones, rename them.
    if column_mappings:
        df = df.rename(columns=column_mappings)

    return df