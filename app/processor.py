from collections import Counter
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


class Processor:

    def __init__(self, df : pd, blacklist : set, text_col_name = "Text"):
        self.df = df
        self.blacklist = blacklist
        self.text_col_name = text_col_name


    def processor(self, blacklist):
        self.df["common_word"] = self.df[self.text_col_name].apply(Processor._find_least_common_word)
        self.df["word_in_blacklist"] = self.df[self.text_col_name].apply(self._find_word_in_blacklist)
        self.df["text_sentiment"] = self.df[self.text_col_name].apply(Processor.classify_sentiment)


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


    @staticmethod
    def classify_sentiment(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score >= 0.5:
            return "Positive"
        elif score <= -0.5:
            return "Negative"
        else:
            return "Neutral"