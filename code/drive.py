# Libraries
import pandas as pd


class Drive:
    def __init__(self):
        self.dcube = None
        self.faces = {'w': ['r', 'g', 'o', 'b'],
                      'g': ['r', 'y', 'o', 'w'],
                      'y': ['r', 'b', 'o', 'g'],
                      'b': ['r', 'w', 'o', 'y'],
                      'r': ['y', 'g', 'w', 'b'],
                      'o': ['w', 'g', 'y', 'b'],
                      }

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
                self.__move_face('w')
        elif move[0] == 't':
            for i in range(int(move[1])):
                self.__move_face('r')
        elif move[0] == 'd':
            for i in range(int(move[1])):
                self.__move_face('o')
        elif move[0] == 'l':
            for i in range(int(move[1])):
                self.__move_face('b')
        elif move[0] == 'r':
            for i in range(int(move[1])):
                self.__move_face('g')
        elif move[0] == 'b':
            for i in range(int(move[1])):
                self.__move_face('y')
        return self

    def __move_face(self, face):
        new_dcube = self.dcube.copy()
        # Front face permutation
        new_dcube[face][0] = self.dcube[face][6]
        new_dcube[face][1] = self.dcube[face][3]
        new_dcube[face][2] = self.dcube[face][0]
        new_dcube[face][3] = self.dcube[face][7]
        new_dcube[face][5] = self.dcube[face][1]
        new_dcube[face][6] = self.dcube[face][8]
        new_dcube[face][7] = self.dcube[face][5]
        new_dcube[face][8] = self.dcube[face][2]
        # Up face permutation
        color_a, color_b = (self.faces[face][0], self.faces[face][-1])
        new_dcube[color_a][6] = self.dcube[color_b][8]
        new_dcube[color_a][7] = self.dcube[color_b][5]
        new_dcube[color_a][8] = self.dcube[color_b][2]
        # Right face permutation
        color_a, color_b = (self.faces[face][1], self.faces[face][0])
        new_dcube[color_a][0] = self.dcube[color_b][6]
        new_dcube[color_a][3] = self.dcube[color_b][7]
        new_dcube[color_a][6] = self.dcube[color_b][8]
        # Down face permutation
        color_a, color_b = (self.faces[face][2], self.faces[face][1])
        new_dcube[color_a][0] = self.dcube[color_b][6]
        new_dcube[color_a][1] = self.dcube[color_b][3]
        new_dcube[color_a][2] = self.dcube[color_b][0]
        # Left face permutation
        color_a, color_b = (self.faces[face][3], self.faces[face][2])
        new_dcube[color_a][2] = self.dcube[color_b][0]
        new_dcube[color_a][5] = self.dcube[color_b][1]
        new_dcube[color_a][8] = self.dcube[color_b][2]
        # Apply permutation
        self.dcube = new_dcube
        return self