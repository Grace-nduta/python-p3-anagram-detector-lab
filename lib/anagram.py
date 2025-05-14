# your code goes here!
              
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        sorted_word = sorted(self.word)

        for possible_anagram in possible_anagrams:
            if len(possible_anagram) != len(self.word):
                continue  # Skip words of different lengths
            
            lower_anagram = possible_anagram.lower()
            if lower_anagram == self.word:
                continue  # Skip exact matches
                
            if sorted(lower_anagram) == sorted_word:
                matches.append(possible_anagram)
                
        return matches              
                  
                
