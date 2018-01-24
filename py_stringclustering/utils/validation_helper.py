
# coding=utf-8

import pandas as pd
import py_stringmatching as sm
import numpy as np

"""
This module provides a collection of validation functions.
"""

################################################
### io.read_data validations ###
################################################
def validate_path_to_file(path):
    if path is None or path == '':
        raise TypeError('Empty input file path.')

################################################
### preprocessing.get_sim_scores validations ###
################################################
def validate_get_sim_score_df(df):
    if df is None or (df is not None and not isinstance(df, pd.DataFrame)):
        raise TypeError('Invalid input DataFrame.')

def validate_get_sim_score_blocked_pairs(blocked_pairs):
    if blocked_pairs is not None and not isinstance(blocked_pairs, pd.DataFrame):
        raise TypeError('Invalid input blocked pairs.')

def validate_get_sim_score_tokenizer(tokenizer):
    if tokenizer is None or \
            (tokenizer is not None and \
            not isinstance(tokenizer, sm.tokenizer.tokenizer.Tokenizer)):
        raise TypeError('Invalid input tokenizer.')

def validate_get_sim_score_sim_measure(sim_measure):
    if sim_measure is None or \
            (sim_measure is not None and \
            not isinstance(sim_measure, sm.similarity_measure.similarity_measure.SimilarityMeasure)):
        raise TypeError('Invalid input similarity measure.')

################################################
### preprocessing.get_sim_matrix validations ###
################################################
def validate_get_sim_matrix_df(df):
    if df is None or (df is not None and not isinstance(df, pd.DataFrame)):
        raise TypeError('Invalid input DataFrame.')

def validate_get_sim_matrix_sim_scores(sim_scores):
    if sim_scores is None or (sim_scores is not None and not isinstance(sim_scores, list)):
        raise TypeError('Invalid input similarity scores.')

################################################
### generic_helper.get_clusters validations ###
################################################
def validate_get_clusters_df(df):
    if df is None or (df is not None and not isinstance(df, pd.DataFrame)):
        raise TypeError('Invalid input DataFrame.')

def validate_get_clusters_labels(labels):
    if labels is None or (labels is not None and not isinstance(labels, np.ndarray)):
        raise TypeError('Invalid input cluster labels.')


