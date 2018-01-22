
# coding=utf-8

def validate_path_to_file(path):
    if path is None or path == '':
        raise TypeError('Empty input file path.')
