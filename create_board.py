#!/usr/bin/env python3

class GameBoard:
    """This class represents a game board"""
    # def __init__(self):
    #     self.name = name
    def generate_board(self, row):
        self.row = row
        game_board = ''
        i = 0
        while i < row:
            game_board += '|  |  |  | \n'
            i += 1
        return game_board
