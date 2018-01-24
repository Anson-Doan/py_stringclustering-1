
# coding=utf-8

from __future__ import unicode_literals
import os

import unittest

from py_stringclustering.utils.generic_helper import get_install_path

from nose.tools import *

import py_stringmatching as sm
import py_stringsimjoin as ssj
from sklearn.cluster import AgglomerativeClustering

from py_stringclustering.io import read_data
from py_stringclustering.preprocessing import get_sim_scores
from py_stringclustering.preprocessing import get_sim_matrix
from py_stringclustering.utils.generic_helper import get_clusters

datasets_path = os.sep.join([get_install_path(), 'tests', 'test_datasets'])
path_big_ten = os.sep.join([datasets_path, 'big_ten.txt'])

class GenericHelperTestCases(unittest.TestCase):
    def setUp(self):
        self.df = read_data(path_big_ten)
        self.trigramtok = sm.QgramTokenizer(qval=3)
        self.blocked_pairs = ssj.jaccard_join(self.df, self.df, 'id', 'id', 'name', 'name', self.trigramtok, 0.3)
        self.jaccsim = sm.Jaccard()
        self.sim_scores = get_sim_scores(self.df, self.blocked_pairs, self.trigramtok, self.jaccsim)
        self.sim_matrix = get_sim_matrix(self.df, self.sim_scores)
        self.aggcl = AgglomerativeClustering(n_clusters=5, affinity='precomputed', linkage='complete')
        self.labels = self.aggcl.fit_predict(self.sim_matrix)


    def tearDown(self):
        return
    
    @raises(TypeError)
    def test_get_clusters_df_none(self):
        get_clusters(None, self.labels)

    @raises(TypeError)
    def test_get_clusters_df_invalid_type(self):
        get_clusters(set(), self.labels)


