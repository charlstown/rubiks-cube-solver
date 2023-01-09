#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: Rubiks Cube Solver
# Author/s: Carlos Grande
# -----------------------------------------------------
# Date: 03/01/2023
# License: MIT
# Version: 0.1.0
# Maintainer/s: Carlos Grande
# Environment: .rubiks-cube-solver/
# -----------------------------------------------------

# Libraries
import logging
import time
import sys
import argparse
import json
import yaml
from io import StringIO
import subprocess

# Classes
from cube import Cube
from visualizer import Viz
from drive import Drive
from pop_up import PopUp


class App:
    """
    APP Class acting as an orchestrator calling other classes.
    Methods:
        - run
        - __auto_move
        - _interface
    """

    def __init__(self, args: argparse.Namespace):
        """
        Constructor from APP class to read the config file, generate the instances from modules
        and declare global variables.
        :param dir_config: path with the configuration file.
        :param dir_face_map: path with the face mapper file.
        :param dir_cube_saved: path with the data of the cube resolved.
        """
        # Argument variables
        dir_config = args.config
        dir_face_map = args.mapping
        dir_cube_saved = args.cube
        arg_level = args.log[0]

        # Reading the config json file
        yaml_file = open(dir_config, 'r', encoding='utf8')
        self.config = yaml.safe_load(yaml_file)

        # Getting logger
        logger = self._get_logger(level=arg_level)

        # Logging argument variables
        logger.debug('')
        logger.debug("Initial args: ")
        for k, v in vars(args).items():
            logger.debug(f">> {k}: {v}")
        logger.debug("\n")

        # Reading required data
        with open(dir_face_map) as f:       # Mapped faces
            face_map = json.load(f)
        with open(dir_cube_saved) as f:     # Cube saved
            self.data = json.load(f)

        # Instance
        self.cube = Cube(self.config, self.data)
        self.viz = Viz(self.config)
        self.drive = Drive(self.config, face_map)
        self.popup = PopUp(self.config)

        # Variables
        self.log = logger
        self.time_start = time.time()
        self.console_help = self.config['console_help']
        self.dcube = self.cube.load()
        self.moves_counter = 0

    def _get_logger(self, level: str) -> logging.Logger:
        """
        Method to generate the logger used in the project
        :param level: the level of the logs to output
        :return: the custom logger
        """
        # Setting up the output level
        levels = {'debug': logging.DEBUG,
                  'info': logging.INFO,
                  'warning': logging.WARNING}
        set_level = levels[level]

        # Setting up the logger
        set_log_format = '%(asctime)s [%(levelname)s] %(filename)s - %(funcName)s (L%(lineno)s): %(message)s'
        set_date_format = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(level=set_level,
                            format=set_log_format,
                            datefmt=set_date_format)
        my_logger = logging.getLogger(__name__)

        # Create a file log handler
        file_handler = logging.FileHandler(self.config['path_logs'])
        file_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter(set_log_format)
        file_handler.setFormatter(f_format)

        # Add handlers to the logger
        my_logger.addHandler(file_handler)
        return my_logger

    def run(self):
        """
        This method runs the front and the back as the app orchestrator, managing all calls.
        :return: None
        """
        # Initializing the app
        self.time_start = time.time()
        self.log.info(f"\033[1m[Initializing {self.config['project_name']}]\033[0m")

        # Connecting events to interface
        self.viz.connect_events_to_interface(self._on_press_event)

        # Rendering latest state
        self.log.debug("Rendering the latest saved state from the Cube:")
        self.viz.render(self.dcube, self.moves_counter)

        # Starting the communication interface
        self._interface()

        # Exiting the app
        self._exit_app()

    def _exit_app(self):
        """
        This method close the program
        """
        # Save the state of the cube
        self.cube.save(self.dcube)
        self.log.debug("Rubik\'s cube successfully saved")

        # Exit the app
        end_app = time.time()
        elapsed_time = end_app - self.time_start
        str_elapsed_time = time.strftime('%H:%M:%S.', time.gmtime(elapsed_time))
        self.log.info(f"\033[1m[Exiting {self.config['project_name']} app."
                      f"Total elapsed time: {str_elapsed_time}]\033[0m")
        sys.exit(0)

    def _on_press_event(self, event):
        cmds = self.config['window_moves']
        moves = list(cmds.keys())

        # Check for moves
        if event.key in moves:
            self.dcube = self.drive.move(self.dcube, f'{cmds[event.key]}1')
            self.log.debug("The Cube was updated.")
            self.moves_counter += 1
            self.viz.render(self.dcube, self.moves_counter)

        # Check for reset
        if event.key == 'r':
            self.dcube = self.cube.restart()
            self.moves_counter = 0
            self.viz.render(self.dcube, self.moves_counter)
            self.log.info(f'Cube was restarted after {self.moves_counter} moves.')

        # Check for help
        if event.key == 'h':
            self.viz.show_help()

        # Check for close program
        if event.key == 'q':
            self._exit_app()

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

    def _interface(self):
        """
        This method acts as a front-end to input the commands and interact with the cube.
        :return: None.
        """
        moves = str(list(self.config['console_moves'].keys()))[1:-1]
        intro = f"""Type a move sequence ({moves}), 'r' to reset, 'h' for help or q to quit:\n"""
        inpt = input(intro)
        check = self.drive.check_for_moves(inpt)

        # Input commands
        if inpt != 'c' and check:
            self.dcube = self.drive.move(self.dcube, inpt)
            print("[APP] The Cube was updated")
            self.moves_counter += 1
            self.viz.render(self.dcube, self.moves_counter)
            return self._interface()
        elif inpt == 'h':
            print(self.console_help)
            return self._interface()
        elif inpt == 'r':
            self.dcube = self.cube.restart()
            self.moves_counter = 0
            self.viz.render(self.dcube, self.moves_counter)
            print(f'[APP] Cube was restarted after {self.moves_counter} moves.')
            return self._interface()
        elif inpt == 'x':
            msg = "[APP] Please select the number of random moves to apply:\n"
            moves = int(input(msg))
            self.__auto_move(moves)
            return self._interface()
        elif inpt != 'q' and not check:
            print(f"[APP] Sorry, the command {inpt} is not valid.")
            return self._interface()
        elif inpt == 'q':
            self.log.info('[APP] Quiting the app.')
            self._exit_app()


# Starting the app when main
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", default="rubiks-cube-solver/config/settings.yaml",
                        help="Add the config file path after this flag")
    parser.add_argument("--cube", "-cb", default="data/cube_saved.json",
                        help="Add the config file path after this flag")
    parser.add_argument("--mapping", "-m", default="data/face_map.json",
                        help="Add the config file path after this flag")
    parser.add_argument('--log', "-l",
                        choices=['debug', 'info', 'warning'],
                        default=["info"],
                        nargs="+")
    input_args = parser.parse_args()

    # App execution
    my_app = App(args=input_args)
    my_app.run()
