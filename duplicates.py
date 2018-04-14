import os
import sys
from os.path import join, getsize, exists
from collections import defaultdict


def find_duplicates(dir_path):
    files_and_paths = defaultdict(list)
    for root, dirs, file_names in os.walk(dir_path):
        for name in file_names:
            name_and_size = (name, getsize(join(root, name)))
            files_and_paths[name_and_size].append(root)
    duplicates = {
        file: paths for file, paths in files_and_paths.items()
        if len(paths) > 1
    }
    return duplicates


def print_duplicates(duplicates):
    print('You have {} duplicates:'.format(len(duplicates)))
    for file, paths in duplicates.items():
        name, size = file
        print('File name:', name)
        print('File size:', size)
        print('Paths:')
        for path in paths:
            print(path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')
    dir_path = sys.argv[1]
    print('You are looking for duplicates in', dir_path)
    if not exists(dir_path):
        sys.exit("Directory path doesn't exist")

    duplicates = find_duplicates(dir_path)

    if not duplicates:
        sys.exit('No duplicates')

    print_duplicates(duplicates)
