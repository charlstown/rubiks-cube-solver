# Libraries
import pandas as pd


class Drive:
    def __init__(self):
        self.dcube = None

    def move(self, dcube: pd.DataFrame, inpt: str):
        moves = self.__parser(inpt)
        self.dcube = dcube
        for move in moves:
            self.__apply(move)
        return self.dcube

    @staticmethod
    def __parser(text: str):
        """Convert the input the string to a move sequence"""
        moves = [text[i] + text[i + 1] for i in range(0, len(text), 2)]
        return moves

    def __apply(self, move: str):
        if move[0] == 'f':
            for i in range(int(move[1])):
                self.__front_move()
        elif move[0] == 't':
            pass
        elif move[0] == 'd':
            pass
        elif move[0] == 'l':
            pass
        elif move[0] == 'r':
            pass
        elif move[0] == 'b':
            pass
        return self

    def __front_move(self):
        new_dcube = self.dcube.copy()
        # White face permutation
        new_dcube['w'][0] = self.dcube['w'][6]
        new_dcube['w'][1] = self.dcube['w'][3]
        new_dcube['w'][2] = self.dcube['w'][0]
        new_dcube['w'][3] = self.dcube['w'][7]
        new_dcube['w'][5] = self.dcube['w'][1]
        new_dcube['w'][6] = self.dcube['w'][8]
        new_dcube['w'][7] = self.dcube['w'][5]
        new_dcube['w'][8] = self.dcube['w'][2]
        # Red face permutation
        new_dcube['r'][6] = self.dcube['b'][8]
        new_dcube['r'][7] = self.dcube['b'][5]
        new_dcube['r'][8] = self.dcube['b'][2]
        # Green face permutation
        new_dcube['g'][0] = self.dcube['r'][6]
        new_dcube['g'][3] = self.dcube['r'][7]
        new_dcube['g'][6] = self.dcube['r'][8]
        # Orange face permutation
        new_dcube['o'][0] = self.dcube['g'][6]
        new_dcube['o'][1] = self.dcube['g'][3]
        new_dcube['o'][2] = self.dcube['g'][0]
        # Red face permutation
        new_dcube['b'][2] = self.dcube['o'][0]
        new_dcube['b'][5] = self.dcube['o'][1]
        new_dcube['b'][8] = self.dcube['o'][2]
        # Apply permutation
        self.dcube = new_dcube
        return self
