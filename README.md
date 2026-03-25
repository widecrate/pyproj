# Python Projects

This repository hosts projects created by @reivaxcjk.

Currently, there is a [simple calculator][scalc] and a [budget pokemon][bpoke] game.
No copyright infringement is intended, this is all in good fun for the sake of learning Python.

## Getting Started

You can recreate them by cloning the repository, then creating a virtual environment to install the necessary packages.

The virtual environment in this case was created using Astral's [`uv`][uvweb] tool, so to recreate the repo with `uv` installed, follow this sequence of steps:

1. Clone the repository.
   ```
   git clone https://github.com/reixavcjk/python-projects
   ```
2. Change directory into the repository that was just cloned.
   ```
   cd python-projects
   ```
3. Sync the packages from `pyproject.toml`.
   ```
   uv sync
   ```
4. Activate the virtual environment that was automatically created.
   ```
   source .venv/bin/activate        # on Linux
   ```

Alternatively, if you have `pip` instead:

1. Clone the repository.
   ```
   git clone https://github.com/reixavcjk/python-projects
   ```
2. Change directory into the repository that was just cloned.
   ```
   cd python-projects
   ```
3. Create a new virtual environment in the `.venv` directory.
   ```
   python -m venv .venv
   ```
4. Activate the virtual environment.
   ```
   source .venv/bin/activate        # on Linux
   ```
5. Install the requirements from `requirements.txt`.
   ```
   pip install -r requirements.txt
   ```

[scalc]: ./Simple%20Calculator.py
[bpoke]: ./pokemon%20game.py
[uvweb]: https://astral.sh/uv

## Running the Code

1. For the graphical Simple Calculator:
   ```
   python Simple\ Calculator.py
   ```
   A window containing some calculator buttons should appear.

   You can click buttons to add numbers or operators to the calculation bar, then click `=` to get the answer.
   The calculator currently only supports single additions, multiplications, subtractions, and divisions. You
   will need to click `Clear` after each run to reset the calculator.

2. For the Pokemon Game:
   ```
   python pokemon\ game.py
   ```
   This game runs in your terminal and lets you choose a Pokemon, wander out to battle, and fight another Pokemon.

## Known Bugs

- Calculator cannot handle multiple operations, e.g., `2*3*4`, and does not fail gracefully.
