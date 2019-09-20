#!/bin/bash

CUR_DIR=${PWD##}

## remove procmon
unset PYTHONPATH
unset PATH

if [ ! -f ./.venv2/bin/activate ]; then
    $CUR_DIR/bootstrap_venv.sh
fi

source .venv2/bin/activate

export PYTHONPATH=$CUR_DIR/ntlmaps/lib:$PYTHONPATH
python ntlmaps/main.py "$@"
