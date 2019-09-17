#!/usr/bin/env python3
import random
moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.reflect_count = 0
        self.cycle_count = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class random_player(Player):

    def move(self):
        return random.choice(moves)


class human_player(Player):

    def move(self):
        hp_move = input(f'Make your move, Hombre!:')
        while ((hp_move != 'rock') and
               (hp_move != 'paper') and
               (hp_move != 'scissors')):
            hp_move = input(f'Wrong Move, Hombre! Please enter a valid move:')
        if hp_move == "rock":
            return "rock"
        elif hp_move == "paper":
            return "paper"
        elif hp_move == "scissors":
            return "scissors"


class reflect_player(Player):

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.reflect_count == 0:
            self.reflect_count += 1
            return "paper"
        elif self.reflect_count >= 0:
            return self.their_move


class cycle_player(Player):

    def move(self):
        if self.cycle_count == 0:
            self.cycle_count += 1
            return "rock"
        elif self.cycle_count == 1:
            self.cycle_count += 1
            return 'paper'
        elif self.cycle_count == 2:
            self.cycle_count -= 2
            return "scissors"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1win_count = 0
        self.p2win_count = 0
        self.tie_count = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1win_count += 1
            print("Player One wins, Hombre!\n")
            print("Player One total wins: " + str(self.p1win_count))
            print("Player Two total wins: " + str(self.p2win_count))
            print("Total Draws: " + str(self.tie_count))
        elif beats(move2, move1):
            self.p2win_count += 1
            print("Player Two wins, Hombre!\n")
            print("Player One total wins: " + str(self.p1win_count))
            print("Player Two total wins: " + str(self.p2win_count))
            print("Total Draws: " + str(self.tie_count))
        else:
            self.tie_count += 1
            print("It's a draw, Hombre!\n")
            print("Player One total wins: " + str(self.p1win_count))
            print("Player Two total wins: " + str(self.p2win_count))
            print("Total Draws: " + str(self.tie_count))
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(f"Hola Hombre! Welcome to Rock, Paper, Scissors at El Cortez!")
        cp_choice = input(f"Choose an amigo: Juan, Maria, or Saul: ")
        while ((cp_choice != 'Juan') and
               (cp_choice != 'Maria') and
               (cp_choice != 'Saul')):
            cp_choice = input(f"Please choose a valid amgio, Hombre!: ")
        if cp_choice == 'Juan':
            self.p2 = random_player()
        elif cp_choice == 'Maria':
            self.p2 = reflect_player()
        elif cp_choice == 'Saul':
            self.p2 = cycle_player()
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
            print("Game over!")
        if self.p1win_count == self.p2win_count:
            print(f"It's a draw, Hombre! Try again!")
        elif self.p1win_count >= self.p2win_count:
            print('Player One wins!! Good job, Hombre!')
        elif self.p2win_count >= self.p1win_count:
            print('Player Two wins!! Try again, Hombre!')


if __name__ == '__main__':
    game = Game(human_player(), cycle_player())
    game.play_game()
