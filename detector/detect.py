# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Detect:
    def __init__(self, path):
        self.text = open(path, 'r')

        # 8 most frequent words not occurring in the other 'languages' list
        self.bm_words = ['en', 'de', 'ikke', 'et', 'fra', 'kan', 'jeg', 'seg']
        self.nn_words = ['ikkje', 'dei', 'ein', 'ho', 'eg', 'eit', 'frå', 'berre']
        self.en_words = ['the', 'be', 'and', 'of', 'in', 'to', 'have', 'it']

        self.word_count_en_bm_nn = {'en': 0,
                                    'bm': 0,
                                    'nn': 0}

    def run(self):
        pass