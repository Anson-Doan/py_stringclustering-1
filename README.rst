.. image:: https://travis-ci.org/adelaneh/py_stringclustering.svg?branch=master
  :target: https://travis-ci.org/adelaneh/py_stringclustering

.. image:: https://ci.appveyor.com/api/projects/status/123srwchg7gd6e1d?svg=true
  :target: https://ci.appveyor.com/project/adelaneh/py-stringclustering

.. image:: https://coveralls.io/repos/github/adelaneh/py_stringclustering/badge.svg
  :target: https://coveralls.io/github/adelaneh/py_stringclustering


py_stringclustering
=================

This project seeks to build a Python-based collection of commands for clustering 
a collection of strings.

Given a set of strings D, the goal of
string clustering is to create a partitioning of of D such that every pair of strings 
falling into the same partition refer to the same real-world entity, and furthermore, 
no two strings assigned to different partitions refer to the same real-world entity. 
A typical string clustering session involves six steps:

1. Read the data from secondary storage
2. Blocking: trying to remove obvious non-matching string pairs and reduce the set 
considered for similarity score calculation
3. Calculate pairwise similarity scores between blocked string pairs
4. Generate the similarity matrix based on the result of the previous step
5. Execute a clustering algorithm using the similarity matrix created above
6. Generate string clusters based on the labels assigned by the clustering algorithm

Current clustering packages do not provide easy-to-use, straightforward commands and workflows 
to perform all the above steps. py_stringclustering seeks to support all the steps involved in 
the above workflow.

The package is free, open-source, and BSD-licensed.

Important links
===============

* Project Homepage: https://sites.google.com/site/anhaidgroup/projects/magellan/py_stringclustering
* Code repository: https://github.com/anhaidgroup/py_stringclustering
* Issue Tracker: https://github.com/anhaidgroup/py_stringclustering/issues

Dependencies
============

The required dependencies to build the packages are:

* pandas (provides data structures to store and manage tables)
* numpy (used to store similarity matrices and required by pandas)


Platforms
=========

py_stringclustering has been tested on Linux, OS X and Windows.
