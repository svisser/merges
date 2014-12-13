"""
merges: Merge multiple sorted files
"""
from __future__ import division

import heapq
import argparse
import sys

import six


__version__ = '0.1.0'
__all__ = ['main', '__version__']


def main():
    parser = argparse.ArgumentParser(description='Merge multiple sorted files')
    parser.add_argument('-c', '--col', type=int, default=-1, help='column index (starts from 0)')
    parser.add_argument('-n', '--numeric', action='store_true', help='numeric sort')
    parser.add_argument('--sep', type=str, default=',', help='column separator')
    parser.add_argument('files', metavar='files', type=str, nargs='+', help='input files')

    args = parser.parse_args()
    col = args.col
    numeric = args.numeric
    sep = six.u(args.sep)

    files = [open(filename, 'r') for filename in args.files]

    if col != -1:
        if numeric:
            conv = float
        else:
            conv = str

        tuples = (
            ((conv(line.split(sep)[col]), line) for line in file)
            for file in files
        )
        merged = heapq.merge(*tuples)
        for key, line in merged:
            sys.stdout.write(line)
    else:
        merged = heapq.merge(*files)
        for line in merged:
            sys.stdout.write(line)


if __name__ == '__main__':
    main()
