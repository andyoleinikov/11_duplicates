# Anti-Duplicator

With this script you can find if you have duplicates in specified folder and subfolders.
You will recieve set of duplicates names and sizes.

# Quickstart

Specify the path to the directory when using this script from the command line.

```bash
$ python duplicates.py <path to a directory>
You are looking for duplicates in <path to a directory>
You have <amount of> duplicates:
<file name> <file size>
```


### Example of script launch on Linux, Python 3.5:

```bash

$ python duplicates.py /home
You are looking for duplicates in /home
You have 7 duplicates:
master 41
3ca6dc5aeb211beeab8e7d3ae5858c9cec1690 163
__init__.py 276
axes_rgb.py 387
Catamarca 1109
RECORD 2812
py26compat.py 481

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
