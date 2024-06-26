import random
from round import Round
class Game(object):

    with open('words.txt', 'r') as f:
        raw_words = open('words.txt', 'r').readlines()
        words = list(filter(lambda x: len(x)>=5 and len(x) <= 7, [y.lower().strip() for y in raw_words]))


    def __init__(self) -> None:
        self.game_started = False
        self.game_finished = False

        self.num_current_round = 0
        self.current_round = None

        self.selected_words = []
        self.rounds = []
        self.score = 0
        self.num_guesses_per_round = 3

# Game Methods
    def start_game(self, n_rounds = 3):
        if not self.game_started:
            self.game_started = True
            self.n_rounds = n_rounds
            self._create_new_game(n_rounds)

        # self.next_round()
    
    def end_game(self):
        self.game_finished = True
        print(f"Game Finished. Your Score is {self.score}/{self.n_rounds}.\nHave a Nice Day!")
        return

# Round Methods
    def start_round(self):
        self.num_current_round += 1
        new_word = self._select_new_word()
        self.selected_words.append(new_word)
        new_round = Round(new_word, self.num_current_round, self.num_guesses_per_round)
        self.current_round = new_round
        self.n_rounds_remaining -= 1
        self.current_round.start_round()

    def end_round(self, score, status):
        self.score += score
        self.current_round.finish_round(status)
        self.rounds.append(self.current_round)

# Game Utils
    def check_user_guess(self, guessed_word):
        if self._is_round_in_progress():
            status = self.current_round.next_chance(guessed_word)
            if status is not None:
                # round_score = self.current_round.num_guesses_remaining+1 if status else 0
                round_score = 1 if status else 0
                # print(round_score)
                self.end_round(round_score, status)
                return True
            return False
    
    def num_rounds_remaining(self):
        return self.n_rounds_remaining


# Private Methods
    def _create_new_game(self, n_rounds=3):
        self.score = 0
        self.n_rounds_remaining = n_rounds
        self.selected_words = []

    def _select_new_word(self):
        while True:
            x = random.randint(0, len(Game.words)-1)
            if not Game.words[x] in self.selected_words:
                return Game.words[x]
    
    def _is_correct_guess(self, guessed_word):
        if self.current_round.anagram == guessed_word:
            return True
    
    def _is_round_in_progress(self):
        return False if not self.current_round else self.current_round.is_in_progress()