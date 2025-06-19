# setup.py

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('assets', ['assets/click.mp3', 'assets/win.mp3', 'assets/lost.mp3', 'assets/draw.mp3'])
]
OPTIONS = {
    'argv_emulation': True,
    'includes': ['pygame'],
    'packages': ['game']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
