#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A: organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, string name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> # Student Tests Here (keep this line)

    >>> add_name({'Abe': {2003: 10}}, 2009, 8, 'Abe')
    {'Abe': {2003: 10, 2009: 8}}

    >>> add_name({'Chris': {2001: 10}}, 2001, 14, 'Chris')
    {'Chris': {2001: 10}}

    >>> add_name({}, 2012, 2, 'Randy')
    {'Randy': {2012: 2}}

    >>> add_name({}, 1989, 7, 'Jimmy')
    {'Jimmy': {1989: 7}}
    """

    # adding name to the dict names
    if name not in names:
        names[name] = {}

    info = names[name]
    # adding year to nested dict
    if year not in info:
        info[year] = rank

    return names


def parse_year(filename):
    """
    Given filename, like 'baby-2000.txt'
    extract and return the int year from between
    the dash and the dot, e.g. 2000
    Raises an exception on failure.
    >>> parse_year('baby-2000.txt')
    2000
    >>> parse_year('infant-123.txt')
    123
    >>> parse_year('nope123.txt')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    Exception:...
    """
    # checks for lack of . or - to raise an exception
    if '.' not in filename or '-' not in filename:
        raise Exception('Cannot parse filename:' + filename)

    # use .split() function to return the int version of the date
    parts_1 = filename.split('-')
    parts_2 = parts_1[1]
    parts_3 = parts_2.split('.')
    return int(parts_3[0])


def add_file(names, filename):
    """
    Given a names dict and filename like baby-2000.txt,
    add the file's data to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}
    >>> add_file({'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}, 'small-2010.txt')
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    f = open(filename)
    lines = f.readlines()
    year = parse_year(filename)

    # loop through the lines and strip and split each one into male and female names
    for i in range(len(lines)):
        text = lines[i].strip()
        parts = text.split(',')
        rank = int(parts[0])
        m_name = parts[1]
        f_name = parts[2]
    # add the names to the dict
        add_name(names, year, rank, m_name)
        add_name(names, year, rank, f_name)

    return names

def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    >>> read_files(['small-2000.txt', 'small-2010.txt'])
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    # for all the filenames add them to the names dict
    names = {}
    for filename in filenames:
        add_file(names, filename)
    return names


def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> # Student Tests Here (keep this line)
    >>> search_names({'Aaliyah': {2001: 90}, 'Ayaan': {2003: 91} }, 'aa')
    ['Aaliyah', 'Ayaan']
    >>> search_names({'Mark': {2001: 90}, 'Shark': {2003: 91}, 'Andrew': {2004: 80} }, 'Ark')
    ['Mark', 'Shark']
    >>> search_names({'James':{2001: 90}, 'Candice': {2003: 91}, 'Andrew': {2004: 80} }, 'An')
    ['Andrew', 'Candice']
    """

    # loop through the sorted list of names and add the ones that contain the target string to a target list
    find_names = sorted(names.keys())
    target_list = []
    for firstname in find_names:
        slow = target.lower()
        nlow = firstname.lower()
        if slow in nlow:
            target_list.append(firstname)
    return target_list


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if target != '':
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
