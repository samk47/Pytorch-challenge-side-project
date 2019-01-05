"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['sl_model.pt']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['torch', 'torchvision', 'numpy', 'opencv']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
