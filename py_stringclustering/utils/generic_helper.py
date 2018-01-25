
# coding=utf-8

import os
import numpy as np

from py_stringclustering.utils import install_path

from py_stringclustering.utils.validation_helper import validate_get_clusters_df
from py_stringclustering.utils.validation_helper import validate_get_clusters_labels

def get_clusters(df, labels):
    """Returns clusters of strings based on the input cluster labels of each string in df.

    Args:
        df (DataFrame): The input strings and their IDs.
        labels (array): A NumPy array containing the cluster labels for strings in df.

    Returns:
        A list of string clusters, each cluster is itself a list of strings.

    Raises:
        TypeError : If any of the inputs are invalid
    """

    # Validate input DataFrame
    validate_get_clusters_df(df)

    # Validate input labels
    validate_get_clusters_labels(labels)

    clusters = []
    unique_labels = set(labels)

    for lbl in unique_labels:
        clusters.append([df.loc[jj]['name'] for jj in np.where(labels == lbl)[0]])

    return clusters


def get_install_path():
    path_list = install_path.split(os.sep)
    return os.sep.join(path_list[0:len(path_list) - 1])
