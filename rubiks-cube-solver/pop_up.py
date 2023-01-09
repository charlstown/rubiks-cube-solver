#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------
# Project: rubiks-cube-solver
# Author/s: Carlos Grande
# Maintainer/s: Carlos Grande
# -----------------------------------------------------

# Libraries
import time
import tkinter as tk


class PopUp:
    """
    Define the class
    """
    def __init__(self, config):
        """
        Define method
        """
        self.config = config

    def close_window(self, wndw):
        pass

    def help_window(self):
        """
        Define method
        """
        window = tk.Tk()
        window.title('Help')
        window.geometry('300x100')
        label = tk.Label(window, text='This is a test')
        button = tk.Button(window, text='Close Window', command=self.close_window(window))
        label.pack()
        button.pack
        window.mainloop()
        # time.sleep(10)
        # self.close_window(window)