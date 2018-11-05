#!/usr/bin/env python3

import unittest
from create_board import GameBoard

def display_board(board):
    new_board = ''
    i = 0
    # TODO: see why 4 rows, extra | symbol
    for i in range(len(board)):
        if i % 2 == 0 and i != 0 and i != len(board) - 1:
            new_board += board[i] + '\n'
        # if i == len(board) - 1:
        #     new_board += board[i]
        new_board += board[i] + '  |  '
    return new_board


def player_input():
    user_symbol = ''

    while user_symbol != 'X' and user_symbol != 'O':
        user_symbol = input("What would you like to play as, 'X' or 'O' ? ")

        if user_symbol == 'X' or user_symbol == 'O':
            return user_symbol


def place_marker(board, marker, position):
    pass


def main():
    # test_board = ['X','O','X','O','X','O','X','O','X']
    # print(display_board(test_board))
    player_input()


if __name__ == '__main__':
    main()
