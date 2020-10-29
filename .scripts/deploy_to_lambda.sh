rm *.zip
rm -rf env
python3 -m virtualenv env
source ./env/bin/activate
python setup.py install
deactivate
rm -rf python
mkdir python
cp -r env/lib python
zip -r9 ./python.zip ./python
cd src
zip -r9 ${OLDPWD}/code.zip .
