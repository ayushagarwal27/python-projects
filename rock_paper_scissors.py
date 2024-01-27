import random
import sys


class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')
        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        user_move: str = input('Rock, paper or scissors ? >>').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('-' * 5)
        print(f'You {self.moves[user_move]}')
        print(f'You {self.moves[ai_move]}')
        print('-' * 5)

    def print_score(self):
        print(f'User score: {self.user_score} | AI score: {self.ai_score}')
    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a tie')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.user_score += 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.user_score += 1
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.user_score += 1
        else:
            self.ai_score += 1
            print('AI wins...')
        self.print_score()

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
