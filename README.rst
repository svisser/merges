merges: Merge multiple sorted files
===================================

|travismaster|

.. |travismaster| image:: https://secure.travis-ci.org/box-and-whisker/merges.png?branch=master
   :target: http://travis-ci.org/box-and-whisker/merges

``merges`` is a simple command-line tool merging multiple sorted files with
small memory footprint. It is similar to `mergelog <http://mergelog.sourceforge.net/>`_
which merges and sorts http log files from web servers behind round-robin DNS.

Usage::

    > merges [-h] [-c COL] [-n] [--sep SEP] files [files ...]
    -h, --help         show help message and exit
    -c COL, --col COL  column index (starts from 0)
    --sep SEP          column separator
    -n, --numeric      numeric sort


Examples
========

Merge two log files, assuming fourth columns contains the timestamp and the
files are space-separated::

    merges -c 3 --sep ' ' a.log b.log > merged.log


With ``s3cmd``, ``parallel`` and named pipes, you can download, merge and sort
multiple log files simultaneously::

    (Add example here)


Installation
============

Installing merges is easy::

    pip install merges

or download the source and run::

    python setup.py install
