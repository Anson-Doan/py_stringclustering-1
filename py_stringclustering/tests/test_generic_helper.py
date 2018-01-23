
# coding=utf-8

from __future__ import unicode_literals

import unittest

from nose.tools import *

from py_stringclustering.io import read_data
from py_stringclustering.preprocessing import get_sim_scores
from py_stringclustering.preprocessing import get_sim_matrix
from py_stringclustering.utils.generic_helper import get_clusters

class GenericHelperTestCases(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    @raises(TypeError)
    def test_read_data_input_path_none(self):
        read_data(None)

    @raises(TypeError)
    def test_read_data_input_path_empty_string(self):
        read_data('')

