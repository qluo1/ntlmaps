#!/bin/bash

CUR_DIR=${PWD##}

## remove procmon
unset PYTHONPATH

if [ ! -f ./.localenv/bin/activate ]; then
    $CUR_DIR/bin/bootstrap_venv.sh
else:
    source ./.localenv/bin/activate
fi
exec python ntlmaps/main.py
