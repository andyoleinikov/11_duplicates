# Anti-Duplicator

With this script you can find if you have duplicates in specified folder and subfolders.
You will recieve files names, sizes and paths.

# Quickstart

Specify the path to the directory when using this script from the command line.

```bash
$ python duplicates.py <path to a directory>
You are looking for duplicates in <path to a directory>
You have <amount of> duplicates:
File name: <file name>
File size: <file size>
Paths:
<Path to file>
```


### Example of script launch on Linux, Python 3.5:

```bash

$ python duplicates.py /test/
You are looking for duplicates in /test/
You have 2 duplicates:
File name: __init__.py
File size: 0
Paths:
/test/env/lib/python3.5/site-packages/pip/operations
/test/env/lib/python3.5/site-packages/pkg_resources/_vendor
File name: INSTALLER
File size: 4
Paths:
/test/env/lib/python3.5/site-packages/setuptools-20.7.0.dist-info
/test/env/lib/python3.5/site-packages/pkg_resources-0.0.0.dist-info
/test/env/lib/python3.5/site-packages/pip-8.1.1.dist-info

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
