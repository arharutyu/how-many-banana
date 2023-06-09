#!/bin/bash

pyver="$(command python3 -V)"
pyverminor="${pyver:9:2}"

if [[ "${pyverminor}" > "09" ]]
then 
    python3 -m venv .venv
    source .venv/bin/activate
    python -m ensurepip --upgrade
    python3 -m pip install --upgrade termcolor
    python3 mainoop.py ${1:-banana}
    deactivate
else 
    echo "Please install python version 3.10 or higher at https://installpython3.com/" >&2
    exit 1
fi