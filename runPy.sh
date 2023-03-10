#!/bin/bash

source ./venv/bin/activate

cd $1/py
python $2.py > $2.ans
