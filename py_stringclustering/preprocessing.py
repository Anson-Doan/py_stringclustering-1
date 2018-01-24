
# coding=utf-8

import numpy as np
    
from py_stringclustering.utils.validation_helper import validate_get_sim_score_df
from py_stringclustering.utils.validation_helper import validate_get_sim_score_blocked_pairs
from py_stringclustering.utils.validation_helper import validate_get_sim_score_tokenizer
from py_stringclustering.utils.validation_helper import validate_get_sim_score_sim_measure
from py_stringclustering.utils.validation_helper import validate_get_sim_matrix_df
from py_stringclustering.utils.validation_helper import validate_get_sim_matrix_sim_scores

def get_sim_scores(df, blocked_pairs, tokenizer, sim_measure):
    """Calculates the similarity scores for every pair of strings in blocked_pairs using sim_measure
    Args:
        df (DataFrame): The input strings and their IDs.
        blocked_pairs (DataFrame): A table containing string ID pairs output by the blocking step.
        tokenizer (class): The tokenizer to be used to tokenize strings in df whose IDs appear in blocked_pairs (a tokenizer from py_stringmatching package).
        sim_measure (class): The similarity measure to be calculated on the blocked string pairs (a similarity measures from py_stringmatching package).
    Returns:
        A list of triplets of the form (a, b, sim_ab) where the tuple (a,b) is a string ID pair in blocked_pairs and sim_ab is the similarity of strings in df associated with a and b as measured by sim_measure, possibly using tokenizer.
    """

    # Validate input DataFrame
    validate_get_sim_score_df(df)

    # Validate input blocked pairs
    validate_get_sim_score_blocked_pairs(blocked_pairs)

    # Validate input tokenizer
    validate_get_sim_score_tokenizer(tokenizer)

    # Validate input similarity measure
    validate_get_sim_score_sim_measure(sim_measure)

    sim_scores = []
    tokens = {}

    # If blocked_pairs is None, then return sim of all possible pairs
    if blocked_pairs is None:
        for l_id in range(len(df)):
            l_toks = _tokenize(df, l_id, tokenizer, tokens)

            for r_id in range(l_id + 1, len(df)):
                r_toks = _tokenize(df, r_id, tokenizer, tokens)

                sim_scores.append((l_id, r_id, _calc_sim(df, l_id, r_id, l_toks, r_toks, sim_measure)))

    else:
        print("Blocked pairs provided.")

        # TODO: Replace iterrows with itertuples
        for index, row in blocked_pairs.iterrows():
            l_id, r_id = int(row['l_id']), int(row['r_id'])

            # If the two strings are the same, don't calculate sim; it is 1.
            # If l_id > r_id, don't calculate sim; the pair (r_id, l_id) has showed up before or will show up later.
            if l_id >= r_id:
                continue
            
            # Tokenize the string corr. to l_id; if already have, just retrieve the tokens
            l_toks = _tokenize(df, l_id, tokenizer, tokens)

            # Tokenize the string corr. to r_id; if already have, just retrieve the tokens
            r_toks = _tokenize(df, r_id, tokenizer, tokens)
   
            # Calculate the similarity measure and add the triplet to the result set
            sim_scores.append((l_id, r_id, _calc_sim(df, l_id, r_id, l_toks, r_toks, sim_measure)))

    return sim_scores

def _tokenize(df, _id, tokenizer, tokens):
    # Tokenize the string corr. to _id; if already have, just retrieve the tokens
    if _id not in tokens:
        _toks = tokenizer.tokenize(df.loc[_id]['name'])
        tokens[_id] = _toks
    else:
        _toks = tokens[_id]
   
    return _toks

def _calc_sim(df, l_id, r_id, l_toks, r_toks, sim_measure):
    # If no tokens are provided for (at least one of) the strings, then call the sim measure directly on the strings
    # Otherwise, call the sim measure on the tokens
    if l_toks is None or r_toks is None:
        return sim_measure.get_sim_score(df.loc[l_id]['name'], df.loc[r_id]['name'])
    else:
        return sim_measure.get_sim_score(l_toks, r_toks)

def get_sim_matrix(df, sim_scores):
    """Creates a similarity matrix based on the sim_scores entries. This similarity matrix is in a format consumable by appropriate scikit-learn clustering algorithms as a 'precomputed' similarity matrix.
    Args:
        df (DataFrame): The input strings and their IDs.
        sim_scores (set): A set of triplets of the form (a, b, sim_ab) where the tuple (a,b) is a string ID pair of strings in df, and sim_ab is the similarity strings in df associated with a and b.
    Returns:
        A similarity matrix in the form of a 2-D NumPy array.
    """

    # Validate input DataFrame
    validate_get_sim_matrix_df(df)

    # Validate input similarity scores
    validate_get_sim_matrix_sim_scores(sim_scores)

    sim_matrix = np.zeros([len(df), len(df)])

    for l_id, r_id, sim in sim_scores:
        sim_matrix[l_id, r_id] = sim

    return sim_matrix


