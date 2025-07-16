from setuptools import setup, find_packages

setup(
    name='collection_fc',
    version='0.1',
    description='Simple collection forecasting library',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'collection_fc=collection_fc.cli:main',
        ],
    },
) 