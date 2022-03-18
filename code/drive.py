# Libraries
import pandas as pd
import random


class Drive:
    def __init__(self, face_map):
        self.dcube = None
        self.face_map = face_map

    def move(self, dcube: pd.DataFrame, inpt: str):
        moves = self.__parser(inpt)
        self.dcube = dcube
        for move in moves:
            self.__apply(move)
        return self.dcube

    def random_move(self):
        moves = ['f', 'b', 'u', 'd', 'r', 'l']
        rand_move = str(moves[random.randint(0, 5)])
        rand_int = str(random.randint(1, 4))
        return rand_move + rand_int


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
        mface = self.face_map[face]
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
        color_a, color_b = (list(mface.keys())[0], list(mface.keys())[-1])
        for a, b in zip(mface[color_a], mface[color_b]):
            new_dcube[color_a][a] = self.dcube[color_b][b]
        # Right face permutation
        color_a, color_b = (list(mface.keys())[1], list(mface.keys())[0])
        for a, b in zip(mface[color_a], mface[color_b]):
            new_dcube[color_a][a] = self.dcube[color_b][b]
        # Down face permutation
        color_a, color_b = (list(mface.keys())[2], list(mface.keys())[1])
        for a, b in zip(mface[color_a], mface[color_b]):
            new_dcube[color_a][a] = self.dcube[color_b][b]
        # Left face permutation
        color_a, color_b = (list(mface.keys())[3], list(mface.keys())[2])
        for a, b in zip(mface[color_a], mface[color_b]):
            new_dcube[color_a][a] = self.dcube[color_b][b]
        # Apply permutation
        self.dcube = new_dcube
        return self