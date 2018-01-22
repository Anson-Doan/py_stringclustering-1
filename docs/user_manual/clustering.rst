Clustering Strings
-------------

The py_stringclustering package provides commands to load and cluster a 
collection of strings. For example, the following command loads a collection 
of strings from a file stored at path_to_file:

    >>> import py_stringclustering as scl
    >>> df = scl.read_data(path_to_file)

The data is returned in a Pandas DataFrame ``df``, which consists of two 
columns, one column ``name`` consisting of the input strings, and another 
column ``id`` consisting of unique IDs assigned to the input strings. This
DataFrame then can be used to perform blocking, reducing the number of string 
pairs to compute the string similarity measure for. The following example 
shows an example of blocking:

    >>> import py_stringmatching as sm
    >>> trigramtok = sm.QgramTokenizer(qval=3)
    >>> blocked_pairs = ssj.jaccard_join(df, df, ‘id', 'id', 'name', 'name', trigramtok, 0.3)

Please refer to the API reference for more details
