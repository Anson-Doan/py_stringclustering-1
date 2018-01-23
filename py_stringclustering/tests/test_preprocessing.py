
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

    def tearDown(self):
        return
    
    @raises(TypeError)
    def test_get_sim_scores_df_none(self):
        get_sim_scores(None, None, None, None)

    @raises(TypeError)
    def test_get_sim_scores_df_invalid_type(self):
        get_sim_scores(set(), None, None, None)

    @raises(TypeError)
    def test_get_sim_scores_blocked_pairs_invalid_type(self):
        get_sim_scores(self.df, [], None, None)
        

