#!/bin/bash

pyver="$(command python3 -V)"
pyverminor="${pyver:9:2}"

if [[ "${pyverminor}" > "09" ]]
then 
    python3 -m venv .venv
    source .venv/bin/activate
    #pip package install here if needed
    python3 mainoop.py
    deactivate
else 
    echo "Please install python version 3.10 or higher at https://installpython3.com/" >&2
    exit 1
fi