import random
import time

class Round(object):
    def __init__(self, word, round_num, num_guesses) -> None:
        self.anagram = word
        self.shuffled_word = "".join(random.sample(self.anagram, len(self.anagram)))
        self.in_progress = False
        self.round_num = round_num
        self.time_started = time.time()
        self.num_guesses = 3
        self.num_guesses_remaining = self.num_guesses
    
    def start_round(self):
        self.in_progress = True
        print(f"Round {self.round_num} Started. {self.num_guesses_remaining} guesses remaining. {self.shuffled_word}")
    
    def is_correct_guess(self, guess_word):
        return guess_word == self.anagram

    def next_chance(self, guess_word):
        if self.is_in_progress():
            self.num_guesses_remaining -= 1

            if self.is_correct_guess(guess_word):
                return True
            if self.num_guesses_remaining == 0:
                return False
            if self.num_guesses_remaining == 1:
                clue = self._get_clue()
                print(f"\r\nWrong! Last guess remaining. {clue}")
            else:
                # shuffled_word = "".join(random.sample(self.anagram, len(self.anagram)))
                print(f"\r\nWrong! {self.num_guesses_remaining} guesses remaining. {self.shuffled_word}")
            return None
    
    def finish_round(self, status):
        if self.is_in_progress():
            if status == 0:
                print(f"Wrong Guesses!!. Correct word is {self.anagram}\n")
            elif status == 1:
                print(f"Correct!! Word is {self.anagram}\n")
            self.in_progress=False
            self.time_ended = time.time()
            self.time_elapsed = self.time_started - self.time_ended

    def is_in_progress(self):
            return self.in_progress
    
    # Private Method
    def _get_clue(self):
        clue_word = ['*'] * len(self.anagram)
        clue_indices = random.sample([y for y in range(len(self.anagram))], min(len(self.anagram)//2, 3))
        for idx in clue_indices:
            clue_word[idx] = self.anagram[idx]
        return " ".join(clue_word)