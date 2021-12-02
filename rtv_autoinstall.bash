#!/bin/bash

cd tools
rm -r dist/odrive-*
python3 setup.py sdist
sudo pip3 install dist/odrive-*
