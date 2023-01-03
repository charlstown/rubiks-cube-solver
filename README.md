# Rubik's Cube Solver in Python

[![python](https://img.shields.io/badge/python-3.10-blue.svg?style=flat&logo=python&logoColor=blue)](https://pypi.org/project/cookiecutter/)
[![license](https://img.shields.io/badge/license-mit-green.svg?logo=cachet&style=flat&logoColor=green)](https://choosealicense.com/licenses/)
[![My Site](https://img.shields.io/badge/about%20me-carlosgrande.me-red?style=flat&logo=aboutdotme&logoColor=red)](https://carlosgrande.me/)

A python project to interact, render and solve a Rubik's cube using a variety of algorithms. It features an interactive 3D display where you can input your custom moves, as well as a solver to calculate the permutations needed to achieve a valid solution.

</br>

<details><summary><b>Readme contents</b></summary>

- [1. Description](#1-Description)
- [2. Installation](#2-Installation)
- [3. Usage](#3-Usage)
- [4. Troubleshooting](#4-Troubleshooting)
- [5. Disclaimer](#5-Disclaimer)
- [6. Help wanted](#6-Help-wanted)
- [7. Other links](#7-Other-links)

</details>

</br>

![Logo](docs/assets/logo_150.png)

</br>

*Repository url:* https://github.com/https://github.com/charlstown/rubiks-cube-solver

---

## 0. Description

A python project to interact, render and solve a Rubik's cube using an object-oriented approach. It features an interactive 3D display where you can input your custom moves, as well as a solver to calculate the permutations needed to achieve a valid solution.


## 1. Installation

### Installing python 3

Make sure you have python 3.x.x installed in your computer. You can get the latest release from the official website: 

https://www.python.org/downloads/

- Windows: https://www.python.org/downloads/windows/
- Linux/UNIX: https://www.python.org/downloads/source/
- Mac OS X: https://www.python.org/downloads/mac-osx/



If you want to check your python version installed you can type the following codes in your computer:

- Windows:

  1. WinKey + R

  2. Type 'cmd'  and press ENTER

  3. Type 'python3 --version' in the console and press ENTER

     ```
     python3 --version
     output: Python 3.6.9
     ```

- Linux/UNIX:

  1. Press CTRL + ALT + T

  2. Type $ python3 --version and press ENTER

     ```
     $ python3 --version
     output: Python 3.6.9
     ```

     

- Mac OS X: 

  1. Go to Applications/Utilities

  2. Click Terminal

  3. Type $ python3 --version and press ENTER

     ```
     $ python3 --version
     output: Python 3.6.9
     ```



### Downloading the repository

Download the repository with the following files:

- code
  - main.py
  - cube.py
  - drive.py
  - visualizer.py
- data
  - config.json
  - cube_done.json
  - cube_saved.json
  - face_map.json
- README.md
- requirements.txt
- Conduct.md
- Documentation.md
- LICENSE.txt



## 2. Usage

Before continue make sure you have installed the libraries from the requirements.txt file.

- Start up the program:

  ```
  $ python .\code\main.py
  ```

  *Output:*

  ```
  Initial args:
  - config: data/config.json
  - cube: data/cube_saved.json
  - mapping: data/face_map.json
  [APP] Initializing the Rubik's Cube
  [APP] Rendering the latest saved state from the Cube:
  Please insert a face to move (f, t, d, r, l, b) or type 'r' to reset or 'h' for help:
  ```

  

##  3. Troubleshooting

Plese open a new issue if you see the script is no working or any additional requirement is needed.

## 4. Disclaimer

This is a proof of concept of a Rubik's Cube model done in Python. This is intended for educational purpose only.

Do not use this for any commercial nor redistribution purpose. Actually, the use of such tool might be allowed for private read-only use, as this is what happens when crawling Whatsapp, but not beyond. I do not take responsibility for any use of this tool.

## 5. Help Wanted

This repository does provide the required python version, you should install it by your own

## 6. Other links

To find more projects, resources, articles and more you can visit my site http://carlosgrande.me/
