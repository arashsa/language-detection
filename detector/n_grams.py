# !/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import string
import collections
from checks import is_number


class NGram():
    """
    A simple class for creating bigrams (should be modified to do variable length n-grams)
    """
    def __init__(self, path, output):
        self.bigrams = {}
        self.total_words = 0

        self.read_path(path)
        self.save_to_file = open(output, 'w')

    def read_path(self, path):
        """
        Sends each file from a path to read_file
        :param path: path to files
        :return: None
        """
        files = glob.glob(path)

        for name in files:
            self.read_file(name)

    def read_file(self, name):
        """
        Creates a string from file
        :param name: name of file
        :return: None
        """
        current_file = open(name, 'r')
        file_as_string = current_file.read()
        # print 'Reading file {}'.format(current_file)
        self.create_bigram(file_as_string)

    def create_bigram(self, file_as_string):
        """

        :param file_as_string: whole file as string
        :return: None
        """
        word_list = []

        for w in file_as_string.split():
            # removes punctuation and whitespace from word
            word = w.translate(string.maketrans("", ""), string.punctuation).lower().strip()
            # checks if word is number or empty string
            if len(word) > 1 and not is_number(word):
                # print word
                word_list.append(word)
                self.total_words += 1

        for i in range(len(word_list) - 1):
            count = self.bigrams.get((word_list[i], word_list[i + 1]))
            if count:
                self.bigrams[(word_list[i], word_list[i + 1])] = count + 1
            else:
                self.bigrams[(word_list[i], word_list[i + 1])] = 1

    def print_bigrams(self):
        sorted_x = collections.OrderedDict(sorted(self.bigrams.items(), key=lambda t: t[1]))
        for w, count in reversed(sorted_x.items()):
            print '{} {} : {}'.format(w[0], w[1], count)

    def write_to_file(self, cutoff=10):
        """
        Writes the bigrams to file with a cutoff
        :param cutoff: how many items added to the bigrams.txt file
        :return:
        """
        sorted_x = collections.OrderedDict(sorted(self.bigrams.items(), key=lambda t: t[1]))
        for w, total in reversed(sorted_x.items()):
            if total < cutoff:
                break
            self.save_to_file.write('{} {} : {}, {:.3f}\n'.format(w[0], w[1], total,
                                                              (float(total) / self.total_words) * 100))
        self.save_to_file.close()

run = NGram('/Users/arashsaidi/Work/TextLab/Code/DUO_Corpus/Nynorsk/*', 'nn_bigrams.txt')
# run.print_bigrams()
run.write_to_file()