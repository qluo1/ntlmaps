#!/bin/bash

################
## bootstrap virtualenv and create .local
export GS_PYPI_URL="http://pypi.site.gs.com/simple"
export GS_PYPI_HOST="pypi.site.gs.com"

export PYTHONPATH=/gns/mw/lang/python/modules/2.7.2/pip-9.0.1/lib/python2.7/site-packages:/gns/mw/lang/python/modules/2.7.2/setuptools-21.0.0/lib/python2.7/site-packages

# downloading the latest virtualenv binary in your temporary place
/gns/mw/lang/python/modules/2.7.2/pip-9.0.1/bin/pip install -i $GS_PYPI_URL --trusted-host $GS_PYPI_HOST --target=./tmp/myvirtemp virtualenv

# creating your virtual env at ./myenv
/gns/mw/lang/python/python-2.7.2-gns.03/bin/python ./tmp/myvirtemp/virtualenv.py ./.localenv
#/home/luosam/ws/usr/local/bin/python ./tmp/myvirtemp/virtualenv.py ./.localenv

rm -rf ./tmp/myvirtemp
CUR_DIR=${PWD##}

cp $CUR_DIR/bin/pip.conf ./.localenv/

## deploy dependency packages
source ./.localenv/bin/activate
pip install setuptools_scm
pip install -r $CUR_DIR/requirements.txt
