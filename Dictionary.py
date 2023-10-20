"""
@author: Aakash Maurya
"""

import random
from re import match
import json
from difflib import get_close_matches

class Dictionary:
    def __init__(self):
        self.Database = json.load(open("Dictionary.json"))

    def Search(self, word):
        word = word.lower()
        if "_" in word or "-" in word:
            for W in self.Database:
                if match(self.StringToRegEX(word), W):
                    return W + ": " + self.Database[W][0]
        else:
            if word in self.Database:
                return self.Database[word][0]
            elif len(get_close_matches(word, self.Database.keys())) > 0:
                same = get_close_matches(word, self.Database.keys())[0]
                return self.Database[same][0]
            else:
                return ""


    def StringToRegEX(self, word):
        regex = "^"
        same = 0
        for _ in word:
            if match(r'[a-z]', _):
                regex += _
                same =0
            elif match(r'\s', _):
                regex += _
                same = 0
            elif match(r'_', _):
                regex += "\w"
                same = 0
            elif match(r'\d', _):
                regex += _
                same = 0
            elif match(r'-', _):
                if same == 0:
                    regex += "\w*"
                    same = 1
        regex += "$"
        return regex


    def Suggestion(self, word):
        result = ""
        word = word.lower()
        last = word.split(" ")
        related = get_close_matches(last[-1], self.Database.keys(), n=5)
        if len(related) > 0:
            result = related[0].title()
            if len(related) > 1:
                result += " , "
                result += related[1].title()
                if len(related) > 2:
                    result += " , "
                    result += related[2].title()
                    if len(related) > 3:
                        result += " , "
                        result += related[3].title()
                        if len(related) > 4:
                            result += " , "
                            result += related[4].title()
        return result


    def NewWord(self):
        W, M = random.choice(list(self.Database.items()))
        word = W.upper() + "\n\n"
        if type(M) == list:
            for i in range(20, len(M[0]),20):
                word += M[0][i-20:i]
                word += "\n"
            # word += M[0]
        else:
            for i in range(20, len(M),20):
                word += M[i-20:i]
                word += "\n"
        return W, M
        
English = Dictionary()

def StrToPara(sentence, line):
        para = ""
        i = 0
        for w in sentence.split():
            if (len(para + w) - i) < line:
                para += w
                para += " "
            else:
                para += "\n"
                i += line
        return para