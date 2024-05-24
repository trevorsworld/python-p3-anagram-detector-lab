# your code goes here!

class Anagram:
    def __init__(self, word):
        self._word = word.lower()

    def match(self, anagrams):
        word_chars_main = [char for char in self._word]
        matching_words = []
        for word in anagrams:
            word_chars = [char for char in word]
            match_check = sorted(word_chars) == sorted(word_chars_main)
            if match_check:
                matching_words.append(word)
        return (matching_words)