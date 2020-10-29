pip3 install virtualenv
python3 -m virtualenv env
source ./env/bin/activate
sh .scripts/setup.sh
python setup.py develop
