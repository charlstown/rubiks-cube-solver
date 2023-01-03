# Usage

The file that acts as orchestrator of Rubiks Cube Solver is the `main.py` file. It should be always executed from the root path of the project.


## Running code

- **Step 1: Create your virtual environment(optional)**

    This step is optional but recommended, create your virtual environment for this project by the name you typed when generating the custom template. By default is **my-python-project (env_name)**.

- **Step 2: Install the requirements**

    Install the requirements to run the project in the virtual environment by the following command. The only library preconfigured in the requirements is PyYAML, required to read the configuration file.

    ``` bash
    pip install -r requirements.txt
    ```

- **Step 3: run the main.py file**

    Let's start by running the main.py file in debug mode.

    ``` bash
    cd my-python-project
    python src/rubiks_cube_solver/main.py -l debug 
    ```

    ??? "Arguments to run the code"

        When running the code you have the following arguments to modify the behaviour of the program.

        ``` bash
        python src/rubiks_cube_solver/main.py [flags]
        ```

        **Options:**

        `-c <config file path>`, `--config <config file path>`
        Add the config file path after this flag
          
        `-l ['--debug', 'info', 'warning']`, `--log ['debug', 'info', 'warning']`
        Set up de level of the logs promted. By default `info`

        `-t`, `--test`
        A switcher to run conditional tests, by default it's set to false.


    After running the command you should see an output showing the initial arguments and the execution of the public and private methods from the Helpers class.

    ``` title="output"
    << Add some part of the initial output>>
    ```


## Understanding the base code

To get a better understanding of the base code from the template, lets review some important files from the project generated.


### 1. The main.py file

**It is the class acting as an orchestrator of the whole code.**

The main.py file is made of one class called **App** and, the following three methods.

| Methods | Description |
| --- | --- |
| `\__init__` | Constructor method to read the configuration parameters, generate the instances from modules and declare the global variables. |
| `_get_logger` | Method to generate the logger used in the project. |
| `run` | Main method to run the whole app and manage all calls. |


#### 1.1 The *\__init__* method

The *\__init__* method is in charge of declaring the configuration values, define the global variables and, generate the instances from other modules like the helpers class.

``` python title="main.py" linenums="31"
def __init__(self, args: argparse.Namespace):
    """
    Constructor method to read the configuration parameters, generate the instances from modules and declare the global variables
    :param args: arguments from the command input flags
    """
    # Argument variables
    dir_config = args.config
    test = args.test
    arg_level = args.log[0]

    # Reading the config json file
    yaml_file = open(dir_config, 'r')
    config = yaml.safe_load(yaml_file)

    # Getting logger
    logger = self._get_logger(level=arg_level)

    # Logging argument variables
    logger.debug('')
    logger.debug("Initial args: ")
    for k, v in vars(args).items():
        logger.debug(f">> {k}: {v}")
    logger.debug("\n")

    # Global variables
    self.config = config
    self.log = logger

    # Global instances
    self.helpers = Helpers(logger=logger, config=config)
```


#### 1.2 The *run* method

The *run* method acts as the runner of the whole script **here is where everything related with the app happens**. The *run* method is set to start developing your code in the lines 94 and 95.

``` python title="main.py" linenums="94" hl_lines="10 11"
def run(self):
    """
    Main method to run the whole app and manage all calls.
    :return: None
    """
    # Initializing the app
    start_app = time.time()
    self.log.info(f"\033[1m[Initializing {self.config['project_name']}]\033[0m")

    # >>> Start your code here <<<
    self.helpers.public_method()

    # Exiting the app
    end_app = time.time()
    elapsed_time = end_app - start_app
    str_elapsed_time = time.strftime('%H:%M:%S.', time.gmtime(elapsed_time))
    self.log.info(f"\033[1m[Exiting {self.config['project_name']} app."
                    f"Total elapsed time: {str_elapsed_time}]\033[0m")
    sys.exit(0)
```


### 2. The helpers.py file

The `helpers.py` file located at *src/package_name* directory contains an example class template as a guide to call this class and others from the `main.py` file.

When instantiating a class in main.py (class App) we should alway pass the following input parameters:

- **logger:** logger object defined in the main file to promt output messages.
- **config:** configuration parameters from the configuration file `config.yaml`.


``` python title="main.py (instanced class from helpers.py)" linenums="60"
# Global instances
self.example_class = Helpers(logger=logger, config=config)
```

#### 2.1 The *\__init__* method

The *\__init__* method is the constructor method from the *class Helpers*. This method creates an instance from its class and, declare initial parameters and global variables.


``` title="helpers.py" linenums="17"
    def __init__(self, logger: logging.Logger, config: dict):
        """
        Constructor method to create an instance from the class with initial arguments and
        global variables
        :param logger: logger defined in the main file
        :param config: configuration parameters
        """
        # Global variables
        self.logger = logger
        self.config = config
        self.example_global_variable = "Hello World"
```


### 3. The configuration file

The configuration file is located in `/data/config.yaml` this file should contain all the configuration parameters for your code.

``` title="config.yaml"
# Configuration parameters
project_name: "rubiks-cube-solver"
path_logs: data/logs/file.log

# >>> Add your configuration parameters here <<<

```

??? "Mockup configuration parameters"
    There are some mock up configuration parameters as a type reminder. It is recommended to delete these parameters before releasing the code. These parameters don't affect the behaviour of the code.
    ``` python title="config.yaml"
    # ⌄⌄⌄ Example. Not actual parameters, remove before code. ⌄⌄⌄
    example_string: This is an string
    example_integer: 2077
    example_float: 2.077
    example_boolean: True
    example_none: None
    example_list:
    - A
    - B
    - C
    example_dictionary:
    key_a: value_a
    key_b: value_b
    example_set: !!set
    ? a
    ? b
    ? 1
    ? 2
    example_anchor: &my_anchor data_to_duplicate
    example_run_anchor: *my_anchor
    # ⌃⌃⌃ Example. Not actual parameters, remove before code. ⌃⌃⌃
    ```


### 4. The logs file

The logs file is an empty located at '/data/logs/file.log'. This file acts as a history of all the logs generated from the executions. You can change the behaviour of these logs in the `main.py` file at the *_get_logger method*.

``` python title="main.py" linenums="62" hl_lines="22 23 24 25 28"
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
```

</br>