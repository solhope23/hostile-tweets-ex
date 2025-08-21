from collections import Counter
import pandas as pd


class Processor:

    def __init__(self, df : pd, blacklist : set):
        self.df = df
        self.blacklist = blacklist


    def processor(self, blacklist):
        self.df["common_word"] = self.df["Text"].apply(Processor._find_least_common_word)
        self.df["word_in_blacklist"] = self.df["Text"].apply(self._find_word_in_blacklist)


    @staticmethod
    def _find_least_common_word(text):
        words = text.split()
        if not words:
            return None
        counts = Counter(words)
        common_word = min(counts, key=lambda k: words[k])
        return common_word



    def _find_word_in_blacklist(self, text):
        words = text.split()
        for word in words:
            if word in self.blacklist:
                return word
        return None





