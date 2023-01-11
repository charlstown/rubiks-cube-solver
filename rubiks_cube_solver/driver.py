#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: rubiks-cube-solver
# Author/s: Carlos Grande
# Maintainer/s: Carlos Grande
# -----------------------------------------------------

# Classes
from cube import Cube
from visualizer import Viz
from worker import Worker

# Libraries
import pandas as pd
import logging


class Driver:
    """
    Class to orchestrate the actions from the interface to the backend.
    """
    def __init__(self, config: dict, logger: logging.Logger, face_map: dict, saved_cube_state: dict):
        """
        Constructor from class Operator to initialize and declare global variables.
        :param face_map: dictionary with the mapping of faces to move.
        """
        # Instance
        self.cube = Cube(config, saved_cube_state)
        self.worker = Worker(config, face_map)
        self.viz = Viz(config)

        # Global variables
        self.log = logger
        self.config = config
        self.dcube = None
        self.moves = config['console_moves']
        self.dcube = self.cube.load()
        self.moves_counter = 0
        self.console_help = self.config['console_help']

    def start(self, event_listener):
        # Connecting events to interface
        self.viz.connect_events_to_interface(event_listener)

        # Rendering latest state
        self.log.debug("Rendering the latest saved state from the Cube:")
        self.viz.render(self.dcube, self.moves_counter)

    def restart(self):
        self.dcube = self.cube.restart()
        self.viz.render(self.dcube, 0)
        self.log.info(f'Cube was restarted after {self.moves_counter} moves.')
        self.moves_counter = 0

    def help(self):
        self.viz.show_help()

    def exit(self):
        # Save the state of the cube
        self.cube.save(self.dcube)
        self.log.debug("Rubik\'s cube successfully saved")

    def move(self, permutation):
        self.dcube = self.worker.move(self.dcube, permutation)
        self.log.debug("The Cube was updated.")
        self.moves_counter += 1
        self.viz.render(self.dcube, self.moves_counter)

    def random_move(self):
        permutation = self.worker.random_move()
        self.dcube = self.worker.move(self.dcube, permutation)
        self.viz.render(self.dcube, self.moves_counter)
        self.moves_counter += 1