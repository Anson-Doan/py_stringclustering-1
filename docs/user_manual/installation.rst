============
Installation
============

Requirements
------------
* Python 2.7 or Python 3.4+

Platforms
---------
py_stringclustering has been tested on Linux (Ubuntu 15, 16, 17), OS X (Sierra), and Windows 10.

Dependencies
------------
* pandas (provides data structures to store and manage tables)
* numpy (used to store similarity matrices and required by pandas)


Installing Using pip
--------------------
To install the package using pip, execute the following
command::

    pip install -U py_stringclustering


The above command will install py_stringclustering and all of its dependencies.


Installing from Source Distribution
-----------------------------------
Clone the py_stringclustering package from GitHub

    git clone https://github.com/anhaidgroup/py_stringclustering.git

Then,  execute the following commands from the package root::

    python setup.py install

which installs py_stringclustering into the default Python directory on your machine. If you do not have installation permission for that directory then you can install the package in your
home directory as follows::

        python setup.py install --user

For more information see this StackOverflow `link <http://stackoverflow.com/questions/14179941/how-to-install-python-packages-without-root-privileges>`_.

The above commands will install py_stringclustering and all of its
dependencies.
