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
    APP Class acting as an orchestrator calling other classes.
    Methods:
        - run
        - __auto_move
        - __interface
    """

    def __init__(self, dir_config: str, dir_face_map: str, dir_cube_saved: str):
        """
        Constructor from APP class to read the config file, generate the instances from modules
        and declare global variables.
        :param dir_config: path with the configuration file.
        :param dir_face_map: path with the face mapper file.
        :param dir_cube_saved: path with the data of the cube resolved.
        """
        # Reading the face map json file
        with open(dir_config) as f:
            self.config = json.load(f)

        # Reading the face map json file
        with open(dir_face_map) as f:
            face_map = json.load(f)

        # Reading the config json file
        with open(dir_cube_saved) as f:
            self.data = json.load(f)

        # Instance
        self.cube = Cube(self.config, self.data)
        self.viz = Viz(self.config)
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
        This method runs the front and the back as the app orchestrator, managing all calls.
        :return: None
        """
        print("[APP] Initializing the Rubik's Cube")

        # Rendering latest state
        print("[APP] Rendering the latest saved state from the Cube:")
        self.viz.render(self.dcube, self.moves_counter)

        # Starting the communication interface
        self.__interface()

        # Saving the cube
        self.cube.save(self.dcube)
        print("[APP] Rubik\'s cube successfully saved")

        # Closing program
        print("[APP] Program closed")

    def __auto_move(self, repetitions: int):
        """
        This method generates the input number of random moves in the cube.
        :param repetitions: number of moves to repeat.
        :return: None.
        """
        for i in range(repetitions + 1):
            permutation = self.drive.random_move()
            self.dcube = self.drive.move(self.dcube, permutation)
            self.viz.render(self.dcube, self.moves_counter)
            self.moves_counter += 1
            # time.sleep(1)

    def __interface(self):
        """
        This method acts as a front-end to input the commands and interact with the cube.
        :return: None.
        """
        intro = """Please insert a face to move (f, t, d, r, l, b) or type 'r' to reset or 'h' for help:\n"""
        inpt = input(intro)
        check = self.drive.check_for_moves(inpt)

        # Input commands
        if inpt != 'c' and check:
            self.dcube = self.drive.move(self.dcube, inpt)
            print("[APP] The Cube was updated:")
            self.moves_counter += 1
            self.viz.render(self.dcube, self.moves_counter)
            return self.__interface()
        elif inpt == 'h':
            print(self.help)
            return self.__interface()
        elif inpt == 'r':
            self.dcube = self.cube.restart()
            self.moves_counter = 0
            self.viz.render(self.dcube, self.moves_counter)
            print(f'[APP] Cube was restarted after {self.moves_counter} moves.')
            return self.__interface()
        elif inpt == 'x':
            msg = "[APP] Please select the number of random moves to apply:\n"
            moves = int(input(msg))
            self.__auto_move(moves)
            return self.__interface()
        elif inpt != 'c' and not check:
            print(f"[APP] Sorry, the command {inpt} is not valid.")
            return self.__interface()
        elif inpt == 'c':
            print('[APP] Closing the app.')


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default="data/config.json",
                        help="Add the config file path after this flag")
    parser.add_argument("--cube", "-cb", default="data/cube_saved.json",
                        help="Add the config file path after this flag")
    parser.add_argument("--mapping", "-m", default="data/face_map.json",
                        help="Add the config file path after this flag")
    # parser.add_argument("--test", "-t", default=False, action='store_true',
    #                     help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_config = args.config
    arg_cube = args.cube
    arg_map = args.mapping
    print("Initial args:")
    for k, v in vars(args).items():
        print(f"- {k}: {v}")

    # App execution
    my_app = App(dir_config=arg_config, dir_face_map=arg_map, dir_cube_saved=arg_cube)
    my_app.run()
