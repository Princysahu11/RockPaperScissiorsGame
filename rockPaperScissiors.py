import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to Rock Paper Scissor game!')

        self.moves: dict={'rock':'🪨','paper':'📜','scissors' : '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_count : int =0
        self.ai_count : int = 0

    def play_game(self):
        user_moves: str = input('Rock, Paper or Scissors -- ?').lower()

        if user_moves =='exit':
            if self.user_count> self.ai_count:
                print(f'you won with {self.user_count} points')
                print('Thanks for playing!!')
                sys.exit()

        if user_moves not in self.valid_moves:
            print('Invalid move..')
            return self.play_game()

        ai_move: str =random.choice(self.valid_moves)
        self.display_moves(user_moves,ai_move)
        self.check_moves(user_moves, ai_move, self.user_count, self.ai_count)


    def display_moves(self,user_moves:str,ai_move:str):
        print('----')
        print(f'You: {self.moves[user_moves]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')



    def check_moves(self,user_moves:str,ai_move:str,user_count:int,ai_count:int):

        if user_moves == ai_move:
            print('It\'s a tie')
        elif (user_moves == 'rock' and ai_move == 'paper')or(user_moves == 'rock' and ai_move == 'scissors') or(user_moves == 'scissors' and ai_move == 'paper'):

            print('You win!!')
            self.user_count += 1

        else:
            print('Ai Win...')
            self.ai_count += 1
        print(f'your total points are : {self.user_count} & AI total points are : {self.ai_count}')


if __name__ == '__main__':
    obj = RPS()
    while True:
        obj.play_game()