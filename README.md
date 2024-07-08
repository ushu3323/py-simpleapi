# PY-SIMPLEAPI

AM experiment using python's built-in http module to build "simpleapi", a simple package to build an API using decorators to define API routes and handlers, inspired on FastAPI library

# Setup
if you want to run the examples, we recommend to setup first a python enviroment

## Create the enviroment
```
python -m venv .venv
```

## Activate it!
You can source the activation script in bash terminal to activate the enviroment.
Run the following command from the root of this project:

```sh
source .venv/Scripts/activate
```

You should see the name of the enviroment near of the terminal prompt. Might see something like this:
```sh
(.venv)  # <- .venv is the name of the enviroment
ushu3323@USHU-PC MINGW64 /c/Users/ushu3323/Documents/Projects/py-httpserver (main)
$
```

## Update pip
```sh
python -m pip install --upgrade pip
```

## Install `simpleapi` package

To access the package globally, first u need to install it using pip, to do so run the following command

```
pip install .
```

the dot `.` means that it needs to install the current project defined by the `pyproject.toml` file


Now you're ready to run the examples or even better! experiment with it creating your own scripts.. enjoy!