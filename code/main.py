# Libraries
import argparse
import json
import random as rndm

# Classes
import re
import time

from cube import Cube
from visualizer import Viz
from drive import Drive


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    - run
    """

    def __init__(self, face_map, cube_saved):
        """
        Class constructor: Here you should read the config file, generate
        the instances from modules and declare global variables.
        :param path: Explain the dir_config parameter.
        """
        # Reading the face map json file
        with open(face_map) as f:
            face_map = json.load(f)

        # Reading the config json file
        with open(cube_saved) as f:
            self.data = json.load(f)

        # Instance
        self.cube = Cube(self.data)
        self.viz = Viz()
        self.drive = Drive(face_map)

        # Variables
        self.help = """Valid commands:
                    - t: Top side move 1 clockwise.
                    - f: Front side move 1 clockwise.
                    - d: Down side move 1 clockwise.
                    - r: Right side move 1 clockwise.
                    - l: Left side move 1 clockwise.
                    - b: Back side move 1 clockwise.
                    - h: show the help.
                    - s: solve the cube.
                    - c: close the app.
                    """
        self.dcube = self.cube.load()
        self.moves_counter = 0

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        print("APP: Initializing the Rubik's Cube")

        # Rendering latest state
        print("Rendering the latest saved state from the Cube:")
        self.viz.render_2d(self.dcube)
        self.viz.render_3d(self.dcube, self.moves_counter)

        # Manual resolution of the code
        # self.__manual_move(100)

        # Starting the interpreter
        self.__start_commands()

        # Saving the cube
        self.cube.save(self.dcube)
        print("Rubik\'s cube successfully saved")

        # Closing program
        print("Program closed")

    @staticmethod
    def __check_for_moves(inpt):
        if bool(re.search("^([ftdlrb][\\d])+$", inpt)):
            return True
        else:
            return False

    def __reset_cube(self):
        # Reading the config json file
        with open('data/cube_done.json') as f:
            self.data = json.load(f)
        # Restart Cube
        self.cube = Cube(self.data)
        self.dcube = self.cube.load()

    def __manual_move(self, repetitions):
        for i in range(repetitions):
            permutation = self.drive.random_move()
            self.dcube = self.drive.move(self.dcube, permutation)
            self.viz.render_3d(self.dcube, self.moves_counter)
            self.moves_counter += 1
            # time.sleep(1)

    def __start_commands(self):
        intro = """Please insert a face to move (f, t, d, r, l, b) or type 'r' to reset or 'h' for help:\n"""
        inpt = input(intro)
        check = self.__check_for_moves(inpt)
        if inpt != 'c' and check:
            self.dcube = self.drive.move(self.dcube, inpt)
            print("The Cube was updated:")
            self.viz.render_2d(self.dcube)
            self.moves_counter += 1
            self.viz.render_3d(self.dcube, self.moves_counter)
            return self.__start_commands()
        elif inpt == 'h':
            print(self.help)
            return self.__start_commands()
        elif inpt == 'r':
            self.__reset_cube()
            self.moves_counter = 0
            self.viz.render_3d(self.dcube, self.moves_counter)
            print(f'Cube was restarted after {self.moves_counter} moves.')
            return self.__start_commands()
        elif inpt == 'x':
            self.__manual_move(50)
            return self.__start_commands()
        elif inpt != 'c' and not check:
            print(f"Sorry, the command {inpt} is not valid.")
            return self.__start_commands()
        elif inpt == 'c':
            print('Closing the app.')


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--cube", "-c", default="data/cube_saved.json",
                        help="Add the config file path after this flag")
    parser.add_argument("--mapping", "-m", default="data/face_map.json",
                        help="Add the config file path after this flag")
    # parser.add_argument("--test", "-t", default=False, action='store_true',
    #                     help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_cube = args.cube
    arg_map = args.mapping
    print("Initial args:")
    for k, v in vars(args).items():
        print(f"- {k}: {v}")

    # App execution
    my_app = App(face_map=arg_map, cube_saved=arg_cube)
    my_app.run()
