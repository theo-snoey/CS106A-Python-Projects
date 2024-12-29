#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """

    slug = []
    # go through key and add to slug
    for i in range(len(key)):
        if key[i].isalpha() and key[i].lower() not in slug:
            slug.append(key[i].lower())
    # go through ALPHABET and add missing letters to slug
    for ch in ALPHABET:
        if ch not in slug:
            slug.append(ch)
    return slug

def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'D')
    'C'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, ' ')
    ' '
    """

    if ch.lower() in source:
        spot = source.index(ch.lower())
        # return lower case encrypted ch
        if ch.islower():
            return slug[spot]
        # return upper case encrypted ch
        return slug[spot].upper()
    return ch

def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.')
    'Zmc khjd z sgtmcdqanks gd ezkkr.'
    """
    # encrypt each character in a given string
    result = ''
    for ch in s:
        enchar = encrypt_char(source, slug, ch)
        result = result + enchar
    return result

def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.')
    'And like a thunderbolt he falls.'
    """
    return encrypt_str(slug, source, s)

def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    >>> encrypt_file('test-plain.txt', 'z')
    zab
    wxy
    """
    # goes through lines in file and encrypt
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(encrypt_str(ALPHABET, slug, line))

def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    >>> decrypt_file('test-crypt.txt', 'z')
    abc
    xyz
    """
    # goes through lines in file and decrypt
    slug = compute_slug(key)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(encrypt_str(slug, ALPHABET, line))

def main():
    args = sys.argv[1:]
    # encrypt argument
    if args[0] == '-encrypt':
        encrypt_file(args[2], args[1])
    # decrypt argument
    if args[0] == '-decrypt':
        decrypt_file(args[2], args[1])

# Python boilerplate.
if __name__ == '__main__':
    main()
