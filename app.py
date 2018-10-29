#!/usr/bin/env python3
from IPython.display import clear_output

def sample_generate_board(rows):
        game_board = ''
        i = 0
        while i < rows:
            game_board += '|  |  |  | \n'
            i += 1
        return game_board


def main():
    row_input = int(input('How many rows would you like? '))
    # user_letter = input('What will you play as? Choose \'X\' or \'O\' ')
    print(sample_generate_board(row_input))

if __name__ == '__main__':
    main()