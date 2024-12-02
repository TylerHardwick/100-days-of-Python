import random
from tkinter import *
class Word_Counter():
    def __init__(self):
        self.dictionary = []
        self.correct_words = 0
        self.word_end = 5
        self.current_words = []
        self.bookshelf = ["two_cities.txt", "farewelltoarms.txt", "prideandprejudice.txt", "got.txt"]
        self.book = self.bookshelf[random.randint(0,3)]

    def reset_book(self):
        self.book = self.bookshelf[random.randint(0,3)]
    def import_words(self):
        with open(self.book) as data:
            text = data.read()
            words = text.split()
            self.dictionary = words


    def display_words(self, label,end):
        self.current_words = []
        self.import_words()
        self.current_words = self.dictionary[end-5:end]
        self.word_end += 5
        print(self.current_words)
        label.config(text=f"{" ".join(self.current_words)}")






