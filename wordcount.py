#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Kevin Clark with help from Joseph Hafed and JT"

import sys


def create_word_dict(filename):
    dictionary = {}
    with open(filename) as f:
        x = f.read()
        listed = x.split()
        for word in listed:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return dictionary


def print_words(filename):
    dictionary = create_word_dict(filename)
    sorted_dict = sorted(dictionary.keys(), key=lambda x: x.lower())
    for word in sorted_dict:
        print(f'{word} : {dictionary[word]}')


def print_top(filename):
    """Prints the top count listing for the given file."""
    dictionary = create_word_dict(filename)
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
    twenty = sorted_dict[:19]
    for word, value in twenty:
        print(f'{word} : {value}')


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
