#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: rubiks-cube-solver
# Author/s: Carlos Grande
# Maintainer/s: Carlos Grande
# -----------------------------------------------------

# Libraries
import matplotlib
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
matplotlib.interactive(True)


class Viz:
    """
    Class to render and visualize the cube with different representations.
    """
    def __init__(self, config: dict):
        """
        Constructor from Viz class to preconfigure the render methods.
        :param config: Initialize configuration parameters.
        """
        # Initialize configuration parameters
        self.config = config
        self.window_help = self.config['window_help']

        # Initialize visualization parameters
        plt.ion()
        self.surfaces = []
        self.fig = plt.figure()

        # Creating the axes
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Configuring the axes
        self.ax.view_init(elev=30, azim=45)
        plt.grid(False)
        plt.axis('off')

        # Adding title
        plt.title(label="My Rubik's Cube",
                  loc="center",
                  fontstyle='normal')

        # Creating text labels
        props = dict(boxstyle='round', facecolor='#89B5C8', alpha=0.25)
        self.txt_moves = self.ax.text2D(0, 0.95, '0 moves', transform=self.ax.transAxes,
                                        fontstyle='italic', color='grey')
        self.ax.text2D(1, 0.95, "Press 'h' to show help", ha='right',
                                        transform=self.ax.transAxes, fontstyle='italic', color='grey')

        # Creating help window
        self.help_window = False
        self.txt_help = self.ax.text2D(0, 0, '', transform=self.ax.transAxes,
                                        ha='left', va='center',
                                            fontstyle='italic', color='#153543', bbox=props, zorder=10)

    def connect_events_to_interface(self, driver):
        self.fig.canvas.mpl_connect('key_press_event', driver)


    def render(self, cube, counter):
        """
        Renders the cube following the configuration parameters.
        :param cube: data with the cube to render.
        :param counter: number of moves to display in the render.
        :return: None.
        """
        if self.config['render_2d']:
            self.__render_2d(cube, counter)
        if self.config['render_3d']:
            self.__render_3d(cube, counter)

    @staticmethod
    def __render_2d(cube: pd.DataFrame, counter: int = 0):
        """
        Prints a 2D unwrapped render with the actual state of the passed cube variable.
        :param cube: Dataframe with the state of the cube.
        :param counter: number applied of moves.
        :return: None.
        """
        c = cube
        unwrap = f"""
         |{c['r'][0]}|{c['r'][1]}|{c['r'][2]}|
         |{c['r'][3]}|{c['r'][4]}|{c['r'][5]}|
         |{c['r'][6]}|{c['r'][7]}|{c['r'][8]}|
|{c['b'][0]}|{c['b'][1]}|{c['b'][2]}|{c['w'][0]}|{c['w'][1]}|{c['w'][2]}|{c['g'][0]}|{c['g'][1]}|{c['g'][2]}|\
{c['y'][0]}|{c['y'][1]}|{c['y'][2]}|
|{c['b'][3]}|{c['b'][4]}|{c['b'][5]}|{c['w'][3]}|{c['w'][4]}|{c['w'][5]}|{c['g'][3]}|{c['g'][4]}|{c['g'][5]}|\
{c['y'][3]}|{c['y'][4]}|{c['y'][5]}|
|{c['b'][6]}|{c['b'][7]}|{c['b'][8]}|{c['w'][6]}|{c['w'][7]}|{c['w'][8]}|{c['g'][6]}|{c['g'][7]}|{c['g'][8]}|\
{c['y'][6]}|{c['y'][7]}|{c['y'][8]}|
         |{c['o'][0]}|{c['o'][1]}|{c['o'][2]}|
         |{c['o'][3]}|{c['o'][4]}|{c['o'][5]}|
         |{c['o'][6]}|{c['o'][7]}|{c['o'][8]}|
        """
        # Render Unwrapped picture
        print(f'{counter} moves')
        print(unwrap)

    def __gen_geometry(self, cube: pd.DataFrame):
        """
        Generates the geometry from the given cube parameter.
        :param cube: dataframe with the state of the cube.
        :return: None.
        """
        # Adding front
        face_map = {'w': [2, 3, 1], 'r': [2, 1, 3], 'o': [2, 1, 0], 'g': [0, 1, 2], 'b': [3, 1, 2], 'y': [2, 0, 1]}
        for color, code in face_map.items():
            colors = self.__map_colors(cube, color)
            self.__create_faces(code, colors)

    def __map_colors(self, cube: pd.DataFrame, color: str) -> list:
        """
        Map the color by linking the Dataframe with the generation order of the surfaces.
        :param cube: contains a Dataframe with the state of the cube.
        :param color: contains a string with the color of the face is being mapped.
        :return: a list with the colors mapped.
        """
        values = list(cube[color])
        values = [value[0] if value[0] != 'o' else 'orange' for value in values]
        mapping = {'w': [8, 7, 6, 5, 4, 3, 2, 1, 0],
                   'r': [2, 1, 0, 5, 4, 3, 8, 7, 6],
                   'o': [8, 7, 6, 5, 4, 3, 2, 1, 0],
                   'b': [6, 3, 0, 7, 4, 1, 8, 5, 2],
                   'g': [8, 5, 2, 7, 4, 1, 6, 3, 0],
                   'y': [6, 7, 8, 3, 4, 5, 0, 1, 2]}
        colors = [values[i] for i in mapping[color]]
        # colors = ['w', 'r', 'b', 'g', 'w', 'r', 'b', 'g', 'w']
        return colors

    def __create_faces(self, gen_code: list, colors: list):
        """
        Generates the cube by assigning colors and plotting the geometry.
        :param gen_code: order to create the coplanar surfaces.
        :param colors: list with the colors mapped.
        :return: None.
        """
        face = []
        for x in range(0, 3):
            for y in range(0, 3):
                x_points = self.__gen_points(gen_code[0], [x, y])
                y_points = self.__gen_points(gen_code[1], [x, y])
                z_points = self.__gen_points(gen_code[2], [x, y])
                face.append([x_points, y_points, z_points])
        self.__plot_surface(face, colors)

    @staticmethod
    def __gen_points(code: int, var: list) -> np.array:
        """
        Generates the points of each coplanar surface from an array of coordinates.
        :param code: code with the plane situation.
        :param var: coordinates to be defined.
        :return: array with the coordinates of each point.
        """
        if code == 1:
            return np.array([[var[0], var[0]], [var[0] + 1, var[0] + 1]])
        if code == 2:
            return np.array([[var[1], var[1] + 1], [var[1], var[1] + 1]])
        else:
            return np.array([[code, code], [code, code]])

    def __plot_surface(self, face: list, colors: list):
        """
        Plots a single face given the points of each square and the colors.
        :param face: list with the arrays of the points to be ploted [[array][array][...]].
        :param colors: list with the letter of the surface color.
        :return: update the self class variable with the surfaces generated.
        """
        for points, color in zip(face, colors):
            self.surfaces.append(self.ax.plot_surface(points[0], points[1], points[2],
                                                      color=color,
                                                      linewidth=0.5,
                                                      edgecolors='black', zorder=1))
        return self.surfaces

    def __render_3d(self, cube: pd.DataFrame, aux_text=0):
        """
        Render a 3D view of the cube from the given data.
        :param cube: dataframe with the data of the cube.
        :param aux_text: number of applied moves.
        :return: None.
        """
        for surface in self.surfaces:
            surface.remove()
        self.surfaces = []
        self.__gen_geometry(cube)

        # Create axis
        axes = [3, 3, 3]

        # Create Data
        data = np.ones(axes, dtype=bool)
        self.fig.canvas.manager.set_window_title('My Rubiks Cube')

        # Update moves label
        self.txt_moves.set_text(f'{aux_text} moves')

        # Plot figure
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def show_help(self):
        self.help_window = not self.help_window
        if self.help_window:
            self.txt_help.set_text(self.window_help)
            # self.fig.canvas.draw()
        else:
            self.txt_help.set_text('')
