import os
import sys
from os.path import join, getsize, exists


def find_duplicates(filepath):
    files_set = set()
    duplicates = set()
    for root, dirs, files in os.walk(filepath):
        for name in files:
            name_and_size = (name, getsize(join(root, name)))
            if name_and_size in files_set:
                duplicates.add(name_and_size)
                continue
            files_set.add(name_and_size)
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('No path specified')
    filepath = ' '.join(sys.argv[1:])
    print('You are looking for duplicates in', filepath)
    duplicates = find_duplicates(filepath)

    if not exists(filepath):
        sys.exit('Filepath doesn\'t exist')

    elif duplicates == set():
        sys.exit('No duplicates')

    print('You have {} duplicates:'.format(len(duplicates)))
    for name, size in duplicates:
        print(name, size)
