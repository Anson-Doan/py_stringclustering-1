
__version__ = '0.1.0'

import pandas as pd
import py_stringmatching as sm
import py_stringsimjoin as ssj
from sklearn.cluster import AgglomerativeClustering

def read_data(path_to_file):
    """Returns a DataFrame loaded from the file path_to_file. Input strings are stored in the file at path_to_file, one value per line.
    Args:
        path_to_file (str): The input file path.
    Returns:
        A DataFrame with two columns named 'id' and 'name' where each name is an input string and the corresponding id is its unique integer ID.
    """
    yield

def get_sim_scores(df, blocked_pairs, tokenizer, sim_measure):
    """Calculates the similarity scores for every pair of strings in blocked_pairs using sim_measure
    Args:
        df (DataFrame): The input strings and their IDs.
        blocked_pairs (list): A list of string ID pairs output by the blocking step.
        tokenizer (class): The tokenizer to be used to tokenize strings in df whose IDs appear in blocked_pairs (a tokenizer from py_stringmatching package).
        sim_measure (class): The similarity measure to be calculated on the blocked string pairs (a similarity measures from py_stringmatching package).
    Returns:
        A set of triplets of the form (a, b, sim_ab) where the tuple (a,b) is a string ID pair in blocked_pairs and sim_ab is the similarity of strings in df associated with a and b as measured by sim_measure, possibly using tokenizer.
    """
    yield

def get_sim_matrix(df, sim_scores):
    """Creates a similarity matrix based on the sim_scores entries. This similarity matrix is in a format consumable by appropriate scikit-learn clustering algorithms as a 'precomputed' similarity matrix.
    Args:
        df (DataFrame): The input strings and their IDs.
        sim_scores (set): A set of triplets of the form (a, b, sim_ab) where the tuple (a,b) is a string ID pair of strings in df, and sim_ab is the similarity strings in df associated with a and b.
    Returns:
        A similarity matrix in the form of a 2-D NumPy array.
    """
    yield

def get_clusters(df, labels):
    """Returns clusters of strings based on the input cluster labels of each string in df.
    Args:
        df (DataFrame): The input strings and their IDs.
        labels (array): A NumPy array containing the cluster labels for strings in df.
    Returns:
        A list of string clusters, each cluster is itself a list of strings.
    """
    yield


