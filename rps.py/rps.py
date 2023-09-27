import random
import time


moves = ['rock', 'paper', 'scissors']

class Player:
    score = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        pass  

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.behavior = 'Human Player'

    def move(self):
        while True:
            move = input('CHOOSE A MOVE: (rock / paper / scissors) \n').lower()
            if move in moves:
                return move
            else:
                print('Wrong move. Try again!')

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class RepeatPlayer(Player):
    def move(self):
        return 'rock'

class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)  # Call the base class learn method to store opponent's move
        self.my_move = my_move  # Remember the player's move

class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]

def p1_win(move1, move2):
    return (move1 == 'scissors' and move2 == 'paper') or \
           (move1 == 'paper' and move2 == 'rock') or \
           (move1 == 'rock' and move2 == 'scissors')

def p2_win(move1, move2):
    return (move1 == 'paper' and move2 == 'scissors') or \
           (move1 == 'rock' and move2 == 'paper') or \
           (move1 == 'scissors' and move2 == 'rock')

class SingleRound:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        time.sleep(1)
        move1 = self.player1.move()
        time.sleep(0.5)
        print("computer is making a move...")
        time.sleep(1)
        move2 = self.player2.move()
        time.sleep(1)
        print(f'Player 1: {move1}  Player 2: {move2}')

        if p1_win(move1, move2):
            self.player1.score += 1
            print('-- YOU WIN! --\n')
        elif p2_win(move1, move2):
            self.player2.score += 1
            print('-- OH SH*T! --\n')
        else:
            print("-- IT'S A TIE --\n")

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)
        time.sleep(0.5)
        print('       SCORE')
        print(f'Human: {self.player1.score} | Computer: {self.player2.score}\n')

class Match:
    def __init__(self, player1, player2, rounds):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds

    def play(self):
        print('Game starts!\n')
        for round_num in range(self.rounds):
            print(f'Round {round_num + 1}:')
            single_round = SingleRound(self.player1, self.player2)
            single_round.play()

        print('Game over!\n\n')
        time.sleep(1)
        self.player1.score = 0
        self.player2.score = 0

def replay():
    play_again = input("Would you like to play again? (yes/no) ").lower()
    if play_again == "yes":
        print("Restarting the game...\n")
        return True
    elif play_again == "no":
        print("Thanks for playing! Goodbye!\n")
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.\n")
        return replay()

if __name__ == '__main__':
    player_characters = {
        'human': HumanPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer()
    }

    while True:
        print('ROCK, PAPER, SCISSORS - GO!\n')
        time.sleep(1)
        print('Here are the rules of the game: \nRock wins against ' 
              'scissors, paper wins against rock, and scissors wins against paper.\n')

        choice = input('CHOOSE AN OPPONENT: (random / reflect / repeat / cycle)\n').lower()

        if choice in player_characters:
            rounds = int(input('Enter the number of rounds: '))
            match = Match(player_characters['human'], player_characters[choice], rounds)
            match.play()
        else:
            print('Wrong player. Try again!')

        if not replay():
            break
