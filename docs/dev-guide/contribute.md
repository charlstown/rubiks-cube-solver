# Contribute

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.
This guide will help you to contribute in different ways to Rubiks Cube Solver.


## Contributor values

In the interest of fostering an open and welcoming environment, contributors and maintainers pledge to participate with a harassment-free experience for everyone—regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

Examples of behaviors that contribute to creating a positive environment include:

- Use welcome and inclusive language.
- Be respectful of differing viewpoints and experiences.
- Gracefully accept constructive criticism.
- Foster what's best for the community.
- Show empathy for other community members.

Decisions are made based on technical merit and consensus. As contributor aspire to treat everyone equally, and to value all contributions. For more information on best practices, please review the Code of Conduct.


## Types of Contributions

You can contribute to this project in many ways:

### 1. Report Bugs

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- If you can, provide detailed steps to reproduce the bug.
- If you don’t have steps to reproduce the bug, just note your observations in as much detail as you can. Questions to start a discussion about the issue are welcome.


### 2. Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with “bug” is open to whoever wants to implement it.


### 3. Implement Features

Look through the GitHub issues for features. Anything tagged with “enhancement” and “please-help” is open to whoever wants to implement it.

Please do not combine multiple feature enhancements into a single pull request.


### 4. Write Documentation

This project could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

If you want to review your changes on the documentation locally, you can do:

``` bash
pip install -r docs/requirements.txt
mkdocs serve
```

This will compile the documentation, open it in your browser and start watching the files for changes, recompiling as you save.


### 5. Submit Feedback

The best way to send feedback is to file an issue at https://github.com/cookiecutter/cookiecutter/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

Remember that this is a volunteer-driven project, and that contributions are welcome :)


## Set up the code for local development

-> **Step 1:** Fork the repository on GitHub.

-> **Step 2:** Clone your fork locally.

``` bash
git clone https://github.com/charlstown/rubiks-cube-solver.git
```

-> **Step 3:** Install requirements.

``` bash
cd rubiks-cube-solver
pip install -m requirements.txt
```

-> **Step 4:** Create your branch.

``` bash
git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

-> **Step 5:** Commit your changes and push your branch to GitHub.

``` bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

-> **Step 6:** Submit a pull request through the GitHub website.

Go to the [pull request section](https://github.com/charlstown/rubiks-cube-solver/pulls) in the repository and select the `New pull request` button.


## Contributor Guidelines

### 1. Open Issue Guidelines

Before opening an issue, check it meets these guidelines:

- Add a description of the bug, feature request, feedback, etc.
- Add a log, output or Screenshot if possible.
- (optional) Add some tests or previous research if you did it.
- Add version information from your OS, code language, libraries, etc.

### 2. Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

- The pull request should be contained: if it’s too big consider splitting it into smaller pull requests.
- If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.md.
- The pull request must pass all CI/CD jobs before being ready for review.
- If one CI/CD job is failing for unrelated reasons you may want to create another PR to fix that first.


To document your pull request you can follow the next example:

``` markdown 
# Preamble

A new method added to generate pdfs as an output by adding the flag `-p`, `--pdf`.


# Features

- New output format for reports generation
- Logger more detailed

# Minor Changes

- Documentation files updated


# Bugfixes

- Config file with project name fixed to run the raw template


# Release collaborators

@charlstown
```


### 3. Coding Standards

- Use the [PEP8 style guide](https://peps.python.org/pep-0008/)
- Functions should be over classes except in tests
- Use double quotes around strings that are used for interpolation or that are natural language messages.

    ``` python
    message = "This is a string"
    ```

- Use single quotes for small symbol-like strings (but break the rules if the strings contain quotes).

    ``` python
    my_dict = {'MyKey': "This is an example"} 
    ```

- Use triple double quotes for docstrings and add the input and output parameters to it.

    ``` python
    class my_class:
    """
    Class description
    """
        def my_method(key: str, items: dict) -> int:
            """
            Return the element from a dictionary given a key
            :param key: key to be selected
            :param items: dictionary of items
            :return: element of the items with the provided key
            """
            return items[key]
    ```


- Use raw string literals for regular expressions even if they aren't needed.

    ``` python
    re.search(r"(?i)(arr|avast|yohoho)!", message)
    ```

    </br>
