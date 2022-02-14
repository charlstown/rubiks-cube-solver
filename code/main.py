# Libraries
import argparse
import json

# Classes
import re

from cube import Cube
from visualizer import Viz
from drive import Drive


class App:
    """
    Class description: Explain the main class.
    Name the public methods from this class:
    - run
    """

    def __init__(self, path):
        """
        Class constructor: Here you should read the config file, generate
        the instances from modules and declare global variables.
        :param path: Explain the dir_config parameter.
        """
        # Reading the config json file
        with open(path) as f:
            self.data = json.load(f)

        # Instance
        self.cube = Cube(self.data)
        self.viz = Viz()
        self.drive = Drive()

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

    def run(self):
        """
        This method runs the whole app and manage all calls.
        :return:
        """
        print("APP: Initializing the Rubik's Cube")

        # Rendering latest state
        print("Rendering the latest saved state from the Cube:")
        self.viz.render_2d(self.dcube)
        self.viz.render_3d(self.dcube)

        # Starting the interpreter
        self.__start_commands()

        # Saving the cube
        self.cube.save()
        print("Rubik\'s cube successfully saved")

        # Closing program
        print("Program closed")

    @staticmethod
    def __check_for_moves(inpt):
        if bool(re.search("^([ftdlrb][\\d])+$", inpt)):
            return True
        else:
            return False

    def __start_commands(self):
        intro = """Please insert a face to move (f, t, d, r, l, b) or type 'h' for help:\n"""
        inpt = input(intro)
        check = self.__check_for_moves(inpt)
        if inpt != 'c' and check:
            self.dcube = self.drive.move(self.dcube, inpt)
            print("The Cube was updated:")
            self.viz.render_2d(self.dcube)
            return self.__start_commands()
        elif inpt == 'h':
            print(self.help)
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
    parser.add_argument("--cube", "-c", default="data/cube.json",
                        help="Add the config file path after this flag")
    # parser.add_argument("--test", "-t", default=False, action='store_true',
    #                     help="This argument is a switcher, by default is false")
    args = parser.parse_args()

    # Argument variables
    arg_cube = args.cube
    print("Initial args:")
    for k, v in vars(args).items():
        print(f"- {k}: {v}")

    # App execution
    my_app = App(path=arg_cube)
    my_app.run()
