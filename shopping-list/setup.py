from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='shopping-list',
    version='0.1.0',
    description='Sends the shopping list to the phone',
    long_description=readme,
    author='Cristina Botez',
    url='https://github.com/cristina0botez/shopping-list',
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'PyBluez==0.23'
    ],
    dependency_links=[
        'https://github.com/BlackLight/PyOBEX/tarball/master#egg=PyOBEX-0.26'
    ]
)
