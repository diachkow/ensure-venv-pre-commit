#!/usr/bin/env python3
""" Python script to check if virtual environment is activated """

import os
import sys

if os.getenv('VIRTUAL_ENV'):
    print('Virtual environment is activated!')
    sys.exit(0)
else:
    print('Virtual environment is not activated!')
    sys.exit(1)
