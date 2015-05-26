__author__ = 'jeanlouis.mbaka'

import os
from os.path import join, getsize


def get_dir_size_helper(dir_path):
    """
    :param dir_path:
    """
    total_size = 0
    for root, _, files in os.walk(dir_path):
        # compute the size of files in root, and add it to the total
        total_size += sum(getsize(join(root, filename)) for filename in files if filename)
    return total_size


def get_dir_size(dir_path):
    """
    Gives the size of top level directories & files in dir_path.

    :param dir_path: target directory
    :return: dictionary where key = <name of Directory/file>, and value = <size in bytes>
    """
    result = {}
    for root, dirs, files in os.walk(dir_path):
        for directory in dirs:
            result.update({directory: get_dir_size_helper(join(root, directory))})
        result.update({filename: getsize(join(root, filename)) for filename in files})
        break
    return result