# Set Up

This section helps to understand how to set up the project, its requirements and, organization .


## Project contents

The Project directory will have the next structure following the [packaging.python.org](https://packaging.python.org/en/latest/tutorials/packaging-projects/?highlight=src#a-simple-project) rules.

``` bash title="Contents"
rubiks-cube-solver
├── src/rubiks_cube_solver <- Folder with the package code files.
│   ├── __init__.py                     <- Constructor file.
│   ├── main.py                         <- File with the source code.
│   └── helpers.py                      <- Example class with helpers methods.
├── data                                <- Data used for the project.
│   ├── config.yaml                     <- Configuration file.
│   └── logs                            <- Logs folder.
│       └── file.log                    <- Logs file from the project.
├── docs                                <- Documentation folder.
│   └── assets                          <- Folder for images and media.
├── tests                               <- Folder for test files.
│   ├── __init__.py                     <- Constructor file.
│   └── test_run.py                     <- Test example file.
├── Dockerfile                          <- Dockerfile to deploy the project.
├── code_of_conduct.md                  <- Code of conduct file.
├── LICENSE                             <- LICENSE file.
├── README.md                           <- README file.
└── requirements.txt                    <- Requirements file.
```

Visit the [Usage section](/user-guide/usage/) to learn how the project works.