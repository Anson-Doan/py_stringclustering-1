
# coding=utf-8

from __future__ import unicode_literals
import os

import unittest

from py_stringclustering.utils.generic_helper import get_install_path

from nose.tools import *

import py_stringmatching as sm
import py_stringsimjoin as ssj

from py_stringclustering.io import read_data
from py_stringclustering.preprocessing import get_sim_scores
from py_stringclustering.preprocessing import get_sim_matrix

datasets_path = os.sep.join([get_install_path(), 'tests', 'test_datasets'])
path_big_ten = os.sep.join([datasets_path, 'big_ten.txt'])

class PreprocessingTestCases(unittest.TestCase):
    def setUp(self):
        self.df = read_data(path_big_ten)
        self.trigramtok = sm.QgramTokenizer(qval=3)
        self.blocked_pairs = ssj.jaccard_join(self.df, self.df, 'id', 'id', 'name', 'name', self.trigramtok, 0.3)
        self.jaccsim = sm.Jaccard()
        self.sim_scores = get_sim_scores(self.df, self.blocked_pairs, self.trigramtok, self.jaccsim)

    def tearDown(self):
        return
    
    @raises(TypeError)
    def test_get_sim_scores_df_none(self):
        get_sim_scores(None, self.blocked_pairs, self.trigramtok, self.jaccsim)

    @raises(TypeError)
    def test_get_sim_scores_df_invalid_type(self):
        get_sim_scores(set(), self.blocked_pairs, self.trigramtok, self.jaccsim)

    @raises(TypeError)
    def test_get_sim_scores_blocked_pairs_invalid_type(self):
        get_sim_scores(self.df, [], self.trigramtok, self.jaccsim)

    @raises(TypeError)
    def test_get_sim_scores_tokenizer_none(self):
        get_sim_scores(self.df, self.blocked_pairs, None, self.jaccsim)

    @raises(TypeError)
    def test_get_sim_scores_tokenizer_invalid_type(self):
        get_sim_scores(self.df, self.blocked_pairs, set(), self.jaccsim)

    @raises(TypeError)
    def test_get_sim_scores_sim_measure_none(self):
        get_sim_scores(self.df, self.blocked_pairs, self.trigramtok, None)

    @raises(TypeError)
    def test_get_sim_scores_sim_measure_invalid_type(self):
        get_sim_scores(self.df, self.blocked_pairs, self.trigramtok, [])

    @raises(TypeError)
    def test_get_sim_matrix_df_none(self):
        get_sim_matrix(None, self.sim_scores)

    @raises(TypeError)
    def test_get_sim_matrix_df_invalid_type(self):
        get_sim_matrix([], self.sim_scores)

    @raises(TypeError)
    def test_get_sim_scores_sim_measure_none(self):
        get_sim_matrix(self.df, None)

    @raises(TypeError)
    def test_get_sim_scores_sim_measure_invalid_type(self):
        get_sim_matrix(self.df, 23)


