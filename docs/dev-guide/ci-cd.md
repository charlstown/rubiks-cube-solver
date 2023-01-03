# CI/CD with GitHub Actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that helps you automate your software development workflows from within GitHub.

You can review and access to predefined actions in the [Github marketplace](https://github.com/marketplace?category=&query=&type=actions), or create custom actions for your own workflows.


## How to use GitHub actions?

Create a `.github/workflows` folder in your repository and add a `.yml` file with the following content:

``` bash
mkdir -p .github/workflows
touch .github/workflows/run-project.yml
touch .github/workflows/documentation.yml
```

In this example we have created two workflow files, the `run-project.yml` to test our project and the `documentation.yml` to deploy the project documentation from mkdocs.


## Actions YAML structure

The following yaml is a complete GitHub actions for create documentations (check out the comments for each component):

``` yaml  title="documentation.yaml"
# Action to deploy the mkdocs documentation to the branch gh-pages.
name: On Push Deploy Documentation # Name of the workflow
on: push # Events that trigger the workflow
  # push:
  #   branches:
  #     - main
  #     - wip-release

# Jobs
jobs: # Jobs to run
    deploy: # Name of the job
        name: deploy-documentation
        runs-on: ubuntu-latest # Operating system to run the job on
        steps: # Steps to run
        - name: Checkout repo # Name of the step
          uses: actions/checkout@v2 # Action to run
        - name: Set up Python # Name of the step
          uses: actions/setup-python@v2 # Action to run
          with: # Inputs for the action
            python-version: 3.7.13 # Version of Python to use
        - name: Caching # Name of the step
          uses: actions/cache@v2 # Action to run
          with: # Inputs for the action
            path: $/{/{ env.pythonLocation /}/} # Path to cache
            key: $/{/{ env.pythonLocation /}/}-$/{/{ hashFiles('setup.py') /}/}-$/{/{ hashFiles('requirements.txt') /}/} # Key to use for restoring and saving the cache
        - name: Install dependencies # Name of the step
          run: | # Commands to run
            python -m pip install --upgrade pip
            pip install mkdocs
            pip install mkdocs-material
            pip install pymdown-extensions
        - name: Deploy documentation # Name of the step
          run: mkdocs gh-deploy --clean --force --verbose # Command to run
```

</br>