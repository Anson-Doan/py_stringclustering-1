
# coding=utf-8

import pandas as pd

from py_stringclustering.utils.validation_helper import validate_path_to_file

def read_data(path_to_file):
    """Returns a DataFrame loaded from the file path_to_file. Input strings are stored in the file at path_to_file, one value per line.

    Args:
        path_to_file (str): The input file path.

    Returns:
        A DataFrame with two columns named 'id' and 'name' where each name is an input string and the corresponding id is its unique integer ID.

    Raises:
        TypeError : If the input is invalid
    """

    # Validate input file path
    validate_path_to_file(path_to_file)

    # Read the strings from the file at path_to_csv_file and return Dataframe with one column containing the input strings
    df = pd.DataFrame.from_csv(path_to_file, header=None, index_col=None)

    # Rename the column
    df.columns = ['name']

    # Add an ID column to df
    df['id'] = range(0, len(df))

    return df


