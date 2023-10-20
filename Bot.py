"""
@author: Aakash Maurya
"""

import random
import json
from difflib import get_close_matches
from Dictionary import English

class Bot():
    def __init__(self):
        self.Record = json.load(open("Dialogue.json"))

    def Response(self, word):
        word = word.lower()
        if word[:8] == "what is ":
            return English.Search(word[8:])
        if word == "help":
            self.AllCommand()
            return self.Record[word][0]
        if word in self.Record:
            if type(self.Record[word]) == list:
                return self.Record[word][random.randint(0, len(self.Record[word])-1)]
            else:
                return self.Record[word]
        elif len(get_close_matches(word, self.Record.keys())) > 0:
            match = get_close_matches(word, self.Record.keys(), cutoff=0.8)[0]
            if match in self.Record:
                    return self.Record[match][random.randint(0, len(self.Record[match])-1)]
        else:
            return self.Record["error"][0]

    def AllCommand(self):
        print("-----All Available Input-----")
        for com in self.Record:
            print(com)
            # return self.Record[get_close_matches(word, self.Record.keys())]
        #[random.randint(0, len(self.Record[get_close_matches(word, self.Record.keys())])-1)]

    #     elif len(get_close_matches(word, self.Record.keys())) > 0:
    #         self.Record[get_close_matches(word, self.Record.keys())[0]]
    #     else:
    #         return ""

AppBot = Bot()
