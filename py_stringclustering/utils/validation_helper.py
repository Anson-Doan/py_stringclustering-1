
# coding=utf-8

import pandas as pd

def validate_path_to_file(path):
    if path is None or path == '':
        raise TypeError('Empty input file path.')

def validate_get_sim_score_df(df):
    if df is None or (df is not None and not isinstance(df, pd.DataFrame)):
        raise TypeError('Invalid input DataFrame.')

def validate_get_sim_score_blocked_pairs(blocked_pairs):
    if blocked_pairs is not None and not isinstance(blocked_pairs, pd.DataFrame):
        raise TypeError('Invalid input blocked pairs.')


