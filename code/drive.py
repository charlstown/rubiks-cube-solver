# Libraries
import pandas as pd
import random
import re


class Drive:
    """
    Class to map and applies moves to the cube.
    """
    def __init__(self, face_map: dict):
        """
        Constructor from class drive to initialize and declare global variables.
        :param face_map: dictionary with the mapping of faces to move.
        """
        self.dcube = None
        self.face_map = face_map

    @staticmethod
    def check_for_moves(input_move: str) -> bool:
        """
        This method checks if the input move is a valid move.
        :param input_move: parameter passed by the user with the move.
        :return: boolean response if it's a valid or invalid move.
        """
        if bool(re.search("^([ftdlrb][\\d])+$", input_move)):
            return True
        else:
            return False

    def move(self, dcube: pd.DataFrame, inpt: str) -> pd.DataFrame:
        """
        This method parse and apply the whole sequence of moves.
        :param dcube: data with the state of the cube.
        :param inpt: parameter passed by the user with the move.
        :return: updated data with the state of the cube.
        """
        moves = self.__parser(inpt)
        self.dcube = dcube
        for move in moves:
            self.__apply(move)
        return self.dcube

    def random_move(self) -> str:
        """
        This method generates a random move string as input.
        :return: string with the random move generated.
        """
        moves = ['f', 'b', 'u', 'd', 'r', 'l']
        rand_move = str(moves[random.randint(0, 5)])
        rand_int = str(random.randint(1, 4))
        return rand_move + rand_int


    @staticmethod
    def __parser(text: str) -> list:
        """
        This method converts the input string to a sequence of moves.
        :param text: input string with the sequence of moves.
        :return: parsed list with the sequence of moves.
        """
        moves = [text[i] + text[i + 1] for i in range(0, len(text), 2)]
        return moves

    def __apply(self, move: str):
        """
        This method drives and apply the passed move to the selected face.
        :param move: string with the passed move.
        :return: None
        """
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

    def __move_face(self, face: str):
        """
        Move the passed face clockwise.
        :param face: selected face to move.
        :return: self
        """
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
