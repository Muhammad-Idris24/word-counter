# setup.py
from setuptools import setup, find_packages

setup(
    name="word_counter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.0',
    ],
    entry_points={
        'console_scripts': [
            'wordcounter=word_counter.cli:main',
        ],
    },
)