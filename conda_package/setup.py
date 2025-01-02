#!/usr/bin/env python

import os
import shutil


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'mpas_tools', '__init__.py')) as f:
    init_file = f.read()

os.chdir(here)

for path in ['ocean', 'landice', 'visualization', 'mesh_tools']:
    destPath = './{}'.format(path)
    if os.path.exists(destPath):
        shutil.rmtree(destPath)
    shutil.copytree('../{}'.format(path), destPath)

