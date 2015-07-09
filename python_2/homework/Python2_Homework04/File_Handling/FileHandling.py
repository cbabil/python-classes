'''
This module contains a function that return the counts of
unique file extensions in a given directory.
'''

import os
import glob


def count_fileext(path="."):
    '''
    this function finds all files extensions
    in a directory and return a dictionary containing
    a count for each unique file extensions
    '''

    ext = {}
    file_ext = glob.glob("*.*")
    all_exts = [os.path.splitext(file)[1] for file in file_ext if os.path.isfile(file)]
    uniq_exts = tuple(set(all_exts))

    for extension in uniq_exts:
        count = 0
        for raw_ext in all_exts:
            if raw_ext == extension:
                count += 1
        ext.update({extension: count})

    return ext
