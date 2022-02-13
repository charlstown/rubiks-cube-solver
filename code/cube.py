# Libraries
import json
import pandas as pd

class Cube:
    """The cube class represents the rubik's cube"""
    def __init__(self, data: dict):
        """
        Constructor method to generate the initial cube variables.
        :param data: loads the cube data from the json file with the latest saved state.
        """
        self.dcube = pd.DataFrame(data)

    def load(self) -> pd.DataFrame:
        """
        Loads the cube object.
        :return: dcube
        """
        return self.dcube

    def save(self):
        data = self.dcube.to_dict('lists')
        with open('data/cube.json', 'w') as f:
            json.dump(data, f, indent=4)

