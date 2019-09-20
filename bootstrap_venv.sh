#!/bin/bash

unset HTTP_PROXY
unset PYTHONPATH

CURDIR=${PWD##}
VENV=${1:-.venv2}

################
## bootstrap virtualenv and create .local
export GS_PYPI_URL="http://devpi.qaauto.url.gs.com:8040/root/qaauto"
export GS_PYPI_HOST="devpi.qaauto.url.gs.com"

# latest python
PYTHON=/sw/external/python-2.7.15/bin/python

${PYTHON} -m virtualenv ${VENV}

cat > $VENV/pip.conf <<END

[global]
timeout = 60
index-url = ${GS_PYPI_URL}
trusted-host = ${GS_PYPI_HOST}
END

source ${VENV}/bin/activate
# pip-tools
pip install -i $GS_PYPI_URL --trusted-host $GS_PYPI_HOST pip-tools

if [ -f ./requirements.txt ]; then
    pip-sync
fi
