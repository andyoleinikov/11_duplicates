import os
import sys
from os.path import join, getsize, isdir
from collections import defaultdict


def find_duplicates(dir_path):
    files_and_paths = defaultdict(list)
    for root, dirs, file_names in os.walk(dir_path):
        for file_name in file_names:
            file_size = getsize(join(root, file_name))
            files_and_paths[(file_name, file_size)].append(root)

    duplicates = {
        (file_name, file_size): paths for (file_name, file_size), paths
        in files_and_paths.items()
        if len(paths) > 1
    }
    return duplicates


def print_duplicates(duplicates):
    print('You have {} duplicates:'.format(len(duplicates)))
    for (file_name, file_size), paths in duplicates.items():
        print('File name:', file_name)
        print('File size:', file_size)
        print('Paths:')
        print('\n'.join(paths))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')
    dir_path = sys.argv[1]
    if not isdir(dir_path):
        sys.exit('Specified path is not a directory')
    
    print('You are looking for duplicates in', dir_path)
    duplicates = find_duplicates(dir_path)

    if duplicates:
        print_duplicates(duplicates)
    else:
        print('No duplicates')
