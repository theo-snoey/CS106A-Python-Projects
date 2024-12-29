#!/usr/bin/env python3

"""
Stanford CS106A TipTop Project
"""

import sys


def main():
    args = sys.argv[1:]
    # takes filename from argments and calls read_files
    dict = read_file(args[0])
    # take dict from read files and calls prin_dict (which alphebetically prints it)
    print_dict(dict)


def print_dict(dict):
    """
    given a dict, prints all elements alphabetically in format with key on one line then values indented by one space
    """
    # loops through each key in a sorted dict.keys() - like list
    for key in sorted(sorted(dict.keys())):
        print(key)
        # for every key printed out loop through a sorted posters list and print out after a space
        for user in sorted(dict[key]):
            print(' ', user)


def info_to_dict(tags, poster, dict):
    """
    given the information for one line, inputs that information into the dictionary
    """
    for tag in tags:
        if tag not in dict:
            dict[tag] = []
        posters = dict[tag]
        # if not in structure to avoid repeats
        # appends the poster to a posters list within a tags key
        if poster not in posters:
            posters.append(poster)
    return dict


def read_file(filename):
    """
    reads a file of posters and tags and uses a helper function to output a dict
    """
    dict = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            parts = line.split('^')
            # lowercase all of the elements of a line
            infos = list(map(lambda part: part.lower(), parts))
            tags = infos[1:]
            poster = infos[0]
            # calls the helper function to input the elements of one line into the dictionary
            info_to_dict(tags, poster, dict)

    return dict


if __name__ == '__main__':
    main()
