# !/usr/bin/env python
# -*- coding: utf-8 -*-


class NNBigrams():
    def __init__(self):
        self.nn_bigrams = 'nn_bigrams.txt'
        self.nn_bigram_list = []

        self.bb_bigrams = 'bb_bigrams.txt'
        self.bb_bigram_list = []

        self.finished_nn_file = open('nn_bigrams_removed_bb.txt', 'w')

        create_list(self.nn_bigrams, self.nn_bigram_list)
        create_list(self.bb_bigrams, self.bb_bigram_list)
        self.check_and_save(self.nn_bigram_list, self.bb_bigram_list)

    def check_and_save(self, list_a, list_b):
        for w in list_a:
            if w not in list_b:
                self.finished_nn_file.write('{} {} \n'.format(w[0], w[1]))

        self.finished_nn_file.close()


def create_list(path, save_list):
        with open(path) as f:
            for line in f:
                save_list.append((line.split()[0], line.split()[1]))


def print_list(to_print):
        for t in to_print:
            print t


run = NNBigrams()