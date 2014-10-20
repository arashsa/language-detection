# !/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import glob
import os


class Detect:
    """
    A method for detecting Nynorsk words from a list of frequently occurring Nynorsk bi-grams
    """
    def __init__(self, bigrams):
        self.found = open('found_bigrams_in_lbk.txt', 'w')
        self.bigrams = open(bigrams, 'r')
        self.bigrams_list = []

        for line in self.bigrams:
            tuples = line.split()
            self.bigrams_list.append((tuples[0], tuples[1]))

    def find_occurrence_in_file(self, file_to_read):
        text = open(file_to_read, 'r')
        write_to_file = True
        p_word = ''
        count = 0

        for w in text:
            count += 1
            for ww in w.split():
                word = ww.translate(string.maketrans("", ""), string.punctuation).lower().strip()
                test = (p_word, word)
                if test in self.bigrams_list:
                    if write_to_file:
                        self.found.write('File: ' + os.path.basename(file_to_read) + '\n')
                        write_to_file = False
                    self.found.write(str(count) + ': ' + test[0] + ' ' + test[1] + '\n')
                p_word = word


def read_many_files(path):
    files = glob.glob(path)
    run = Detect('nn_bigrams_1000.txt')

    for name in files:
        # print name
        run.find_occurrence_in_file(name)

    run.found.close()

read_many_files('/Users/arashsaidi/Work/LBK - prosjekt/lbk_22.04.14/Periodika/AV01/*.txt')