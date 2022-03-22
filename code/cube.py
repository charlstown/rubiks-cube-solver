# Libraries
import json
import pandas as pd

class Cube:
    """The cube class represents the rubik's cube model.
    Methods:
        - load
        - restart
        - save
    """
    def __init__(self, config: dict, data: dict):
        """
        Constructor method to generate the initial cube variables.
        :param data: loads the cube data from the json file with the latest saved state.
        """
        self.path_cube_done = config['path_cube_done']
        self.dcube = pd.DataFrame(data)

    def load(self) -> pd.DataFrame:
        """
        Loads the cube object.
        :return: returns a Dataframe with the generated cube.
        """
        return self.dcube

    def restart(self) -> pd.DataFrame:
        """
        Restart the cube by loading the solved data from the json file.
        :return: the loaded data from the json file.
        """
        # Reading the config json file
        with open(self.path_cube_done) as f:
            cube_done = json.load(f)
        # Restart Cube
        self.dcube = pd.DataFrame(cube_done)
        return self.dcube

    @staticmethod
    def save(dcube: pd.DataFrame):
        """
        Saves the state of the cube in a json file.
        :param dcube: Dataframe with the data of the state of the cube.
        :return: None.
        """
        data = dcube.to_dict('list')
        with open('data/cube_saved.json', 'w') as f:
            json.dump(data, f, indent=4)

